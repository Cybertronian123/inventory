# inventory/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Item

class ItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {'name': 'Sample Item', 'description': 'Sample Description', 'quantity': 10, 'price': 9.99}
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        response = self.client.post('/api/items/', self.item_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_read_item(self):
        response = self.client.get(f'/api/items/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
