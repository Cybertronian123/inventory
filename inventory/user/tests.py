from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserRegistrationTest(APITestCase):
    def setUp(self):
        # Define the URL for the register endpoint
        self.register_url = reverse('register_user')

        # Sample user data for a new user
        self.valid_user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }

        # Sample user data with a username that already exists
        self.existing_user_data = {
            'username': 'existinguser',
            'email': 'existinguser@example.com',
            'password': 'testpassword123'
        }

        # Create an existing user in the setup
        self.existing_user = User.objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='testpassword123'
        )

    def test_register_user_success(self):
        """
        Test that a user can be successfully registered with valid data.
        """
        response = self.client.post(self.register_url, self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['username'], self.valid_user_data['username'])

    def test_register_user_duplicate_username(self):
        """
        Test that registration fails if the username already exists.
        """
        response = self.client.post(self.register_url, self.existing_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Username already exists')

    def test_register_user_invalid_data(self):
        """
        Test that registration fails with missing or invalid data.
        """
        # Missing password
        invalid_data = {
            'username': 'incompleteuser',
            'email': 'incompleteuser@example.com'
        }
        response = self.client.post(self.register_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)  # Password should be required
