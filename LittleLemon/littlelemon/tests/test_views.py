from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from django.core import serializers
from restaurant.views import MenuItemsView
import json
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_model =  Menu.objects.create(name="Croissant", price=5, description="sweet")
        self.test_model1 = Menu.objects.create(name="CheeseCake", price=10, description="sweet")
        
    def test_get_all(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('menu'))
        
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "Croissant")
        self.assertContains(response, "CheeseCake")
        
    # def test_view_behavior(self):
    #     # Simulate a POST request with data to your view
    #     client = Client()
    #     client.login(username='testuser', password='testpassword')
    #     response = client.post(reverse('menu'), {'name': 'New Item'})  # Replace with your actual view name

    #     # Check that the response status code is 302 (redirect) if applicable
    #     self.assertEqual(response.status_code, 302)

    #     # Check that the view behavior has been applied to the data
    #     self.assertTrue(Menu.objects.filter(name='New Item').exists())
