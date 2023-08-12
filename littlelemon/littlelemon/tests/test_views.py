from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from django.core import serializers

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(Title="Hamburger", Price=10, Inventory=200)
        item2 = Menu.objects.create(Title="Ice Creame", Price=20, Inventory=100)

    def test_getall(self):
        menuObjects = Menu.objects.get(Title='Hamburger')
        self.assertEqual(menuObjects.Price, 10.00)
    