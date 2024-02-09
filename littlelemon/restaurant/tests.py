from django.test import TestCase
from .models import BookingTable, Menu, MenuTableSelection
# Create your tests here.
class TestRestaurant(TestCase):
    def test_restaurant(self):
        booking_table=BookingTable.objects.create(name='Test', nr_of_guests=2)
        menu=Menu.objects.create(title='Test', price=10000, description='TestDescription')
        menu_sopa=Menu.objects.create(title='Sopa de Feijão', price=1500, description='TestDescription2')
        menu_table_selection=MenuTableSelection.objects.create(table_selection=booking_table, inventory=menu, number_of_items=2)
        self.assertEqual(booking_table.name, 'Test')
        self.assertEqual(booking_table.nr_of_guests, 2)
        self.assertEqual(menu.title, 'Test')
        self.assertEqual(menu.price, 10000)
        self.assertEqual(menu.description, 'TestDescription')
        self.assertEqual(menu_sopa.title, 'Sopa de Feijão')
        self.assertEqual(menu_sopa.price, 1500)
        self.assertEqual(menu_sopa.description, 'TestDescription2')
        self.assertEqual(menu_table_selection.table_selection, booking_table)
        self.assertEqual(menu_table_selection.inventory, menu)
        self.assertEqual(menu_table_selection.number_of_items, 2)
