from django.urls import path
from .views import create_item, read_item, update_item, delete_item

urlpatterns = [
    path('items/', create_item),
    path('items/<int:item_id>/', read_item),
    path('items/<int:item_id>/update/', update_item),
    path('items/<int:item_id>/delete/', delete_item),
]
