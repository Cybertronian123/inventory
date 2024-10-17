# inventory/views.py
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
import logging

# Logger setup
logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Item created: {serializer.data['name']}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_item(request, item_id):
    # Check Redis cache first
    item = cache.get(f'item_{item_id}')
    if not item:
        print("DATABASE CALLED")
        item = get_object_or_404(Item, id=item_id)
        cache.set(f'item_{item_id}', item)  # Cache item
        logger.info(f"Item cached: {item.name}")
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.set(f'item_{item_id}', item)  # Update cache
        logger.info(f"Item updated: {serializer.data['name']}")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    cache.delete(f'item_{item_id}')  # Clear cache
    logger.info(f"Item deleted: {item.name}")
    return Response({"message": "Item deleted successfully"}, status=status.HTTP_200_OK)
