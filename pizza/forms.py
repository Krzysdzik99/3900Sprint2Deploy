
from django import forms
from django.forms import ModelForm
from .models import Topping

from .models import store

class PizzaCreate(ModelForm):
    
    class Meta:
        model = Topping
        fields = ('pizza', 'cheese', 'onion', 'tomato','sausage','basil','mushroom','pepper','chicken', 'price')
class StoreCreate(ModelForm):

    class Meta:
        model = store
        fields = ('name','address')




