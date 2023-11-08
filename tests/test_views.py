from django.test import TestCase, Client
from restaurant.models import Menu as MenuItem
from restaurant.views import MenuItemView, SingleMenuItemView

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        response = self.client.get('menu/')
        self.assertEqual(response.status_code, 200)
