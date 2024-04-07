from django import forms
from .models import Booking, MenuItem , MenuSelection,UserModel
# Create your forms here.

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Nombre de usuario')
    password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"