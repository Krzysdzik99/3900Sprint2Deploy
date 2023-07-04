from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Pizza(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE, default=False)
    cheese = models.BooleanField(default=False, verbose_name="Cheese")
    onion = models.BooleanField(default=False, verbose_name="onion")
    tomato = models.BooleanField(default=False, verbose_name="tomato")
    sausage = models.BooleanField(default=False, verbose_name="sausage")
    pepper= models.BooleanField(default=False, verbose_name="pepper")
    chicken = models.BooleanField(default=False, verbose_name="chicken")
    basil = models.BooleanField(default=False, verbose_name="basil")
    mushroom = models.BooleanField(default=False, verbose_name="mushroom")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return str(self.pizza)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

class store(models.Model):
    name = models.CharField(max_length=120, blank = True)
    address = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


    def str(self):
        return self.user.username
