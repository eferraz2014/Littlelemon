from django.test import TestCase
from .models import Booking, MenuItem , MenuSelection,UserModel
# Create your tests here.
class TestRestaurant(TestCase):
    def test_restaurant(self):
        booking_t=Booking.objects.create(name='Test', nr_of_guests=2)
        menu=MenuItem.objects.create(title='Test', price=10000, description='TestDescription')
        menu_sopa=MenuItem.objects.create(title='Sopa de Feijão', price=1500, description='TestDescription2')
        menu_selection=MenuSelection.objects.create(booking=booking_t, menuItem=menu, number_of_items=2)
        user=UserModel.objects.create(username='Test', password='passwordTest', email='emailTest@gmail.com', first_name='FirstTest', last_name='LastTest')
        user2=UserModel.objects.create(username='Test2', password='passwordTest2', email='emailTest2@gmail.com', first_name='FirstTest2', last_name='LastTest2')

        self.assertEqual(booking_t.name, 'Test')
        self.assertEqual(booking_t.nr_of_guests, 2)

        self.assertEqual(menu.title, 'Test')
        self.assertEqual(menu.price, 10000)
        self.assertEqual(menu.description, 'TestDescription')

        self.assertEqual(menu_sopa.title, 'Sopa de Feijão')
        self.assertEqual(menu_sopa.price, 1500)
        self.assertEqual(menu_sopa.description, 'TestDescription2')

        self.assertEqual(menu_selection.booking, booking_t)
        self.assertEqual(menu_selection.menuitem, menu)
        self.assertEqual(menu_selection.number_of_items, 2)

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


        SingleBookingView = self.client.get('/restaurant/reserve-menu/1')
        self.assertEqual(SingleBookingView.status_code, 200)