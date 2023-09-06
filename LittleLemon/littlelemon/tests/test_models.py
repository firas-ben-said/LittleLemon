from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=10, description="sweet")
        self.assertEqual(str(item), "IceCream : 10")
        