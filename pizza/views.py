from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from register import forms
from .forms import PizzaCreate
from .models import Pizza, Topping
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import store
from .forms import StoreCreate


class Homepage(ListView):
    model = Topping
    template_name = 'order_page.html'

class Detailpage(DetailView):
    model = Topping
    template_name = 'detail.html'

class Createpage(LoginRequiredMixin, CreateView):
    model = Topping
    template_name = 'create.html'
    form_class = PizzaCreate
    success_url = reverse_lazy('home')
class CreateStoreee(LoginRequiredMixin, CreateView):
    model = store
    template_name = 'createStore.html'
    form_class = StoreCreate
    success_url = reverse_lazy('home')

class Createpizza(LoginRequiredMixin, CreateView):
    model = Pizza
    template_name = 'create_pizza.html'
    success_url = reverse_lazy('create')
    fields = '__all__'
class CreateStore(LoginRequiredMixin, CreateView):
    model = store
    template_name = 'create_store.html'
    success_url = reverse_lazy('create')
    fields = '__all__'
class UpdatePizza(UpdateView):
    model = Topping
    template_name = 'update.html'
    from_class = PizzaCreate
    fields = ['cheese', 'onion', 'tomato', 'quantity']

class AdminUpdatePizza(LoginRequiredMixin, UpdateView):
    model = Topping
    template_name = 'admin_update.html'
    from_class = PizzaCreate
    fields = '__all__'

class Confirmpage(DetailView):
    model = Topping
    template_name = 'checkout.html'

class DeletePizza(LoginRequiredMixin, DeleteView):
    model = Pizza
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


def userProfile(request):
    return render(request, 'profile.html')

class Buypage(DetailView):
    model = Topping
    template_name = 'buy.html'

    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User

    class UpdateUser(UpdateView):
            model = User
            fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def get_object(self, queryset=None):
        return self.request.user.userprofile


