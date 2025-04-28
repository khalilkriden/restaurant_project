from django import forms
from .models import Dish, Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['dish','date', 'time', 'number_of_people', 'special_request']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
