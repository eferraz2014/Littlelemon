from django.urls import path
from .views import BookingTableView, MenuView, MenuTableSelectionView
from .views import home,about,book,menu,display_menu_item,login_view,add_menu_items

urlpatterns = [
    path('api/booking', BookingTableView.as_view(), name='booking'),
    path('api/menu/', MenuView.as_view(), name='menu'),
    path('api/reserve-menu', MenuTableSelectionView.as_view(), name='reserve-menu'),
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('book', book, name='book'),
    path('menu', menu, name='menu'),
    path('display-menu-item/<int:pk>', display_menu_item, name='display-menu-item'),

    path('login/', login_view, name='login'),
    path('add_menu_items/<int:booking_id>/', add_menu_items, name='add_menu_items'),
]
