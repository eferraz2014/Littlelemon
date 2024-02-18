from django.test import TestCase
from .models import BookingTable, Menu, MenuTableSelection,UserModel
# Create your tests here.
class TestRestaurant(TestCase):
    def test_restaurant(self):
        booking_table=BookingTable.objects.create(name='Test', nr_of_guests=2)
        menu=Menu.objects.create(title='Test', price=10000, description='TestDescription')
        menu_sopa=Menu.objects.create(title='Sopa de Feijão', price=1500, description='TestDescription2')
        menu_table_selection=MenuTableSelection.objects.create(table_selection=booking_table, inventory=menu, number_of_items=2)
        user=UserModel.objects.create(username='Test', password='passwordTest', email='emailTest@gmail.com', first_name='FirstTest', last_name='LastTest')
        user2=UserModel.objects.create(username='Test2', password='passwordTest2', email='emailTest2@gmail.com', first_name='FirstTest2', last_name='LastTest2')
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
        self.assertEqual(user.username, 'Test')
        self.assertEqual(user.password, 'passwordTest')
        self.assertEqual(user.email, 'emailTest@gmail.com')
        self.assertEqual(user.first_name, 'FirstTest')
        self.assertEqual(user.last_name, 'LastTest')
        
        self.assertEqual(user2.username, 'Test2')
        self.assertEqual(user2.password, 'passwordTest2')
        self.assertEqual(user2.email, 'emailTest2@gmail.com')
        self.assertEqual(user2.first_name, 'FirstTest2')
        self.assertEqual(user2.last_name, 'LastTest2')
