from django.urls import path
from .views import MenuItemView,SingleMenuItemView
from .views import home,about,book,menu,display_menu_item,login_view,logout_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('restaurant/menu', MenuItemView.as_view(), name='menu'),
    path('restaurant/menu/<int:pk>', SingleMenuItemView.as_view(), name='single-menu'),

    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),

    path('home', home, name='home'),
    path('about', about, name='about'),
    path('book', book, name='book'),
    path('menu', menu, name='menu'),
    path('display-menu-item/<int:pk>', display_menu_item, name='display-menu-item'),
    path('api/api-token-auth', obtain_auth_token, name='api_token_auth'),
]