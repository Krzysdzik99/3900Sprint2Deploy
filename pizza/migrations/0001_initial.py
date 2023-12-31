# Generated by Django 4.2.2 on 2023-06-19 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('payment_info', models.CharField(blank=True, max_length=100)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheese', models.BooleanField(default=False, verbose_name='Cheese')),
                ('onion', models.BooleanField(default=False, verbose_name='onion')),
                ('tomato', models.BooleanField(default=False, verbose_name='tomato')),
                ('sausage', models.BooleanField(default=False, verbose_name='sausage')),
                ('pepper', models.BooleanField(default=False, verbose_name='pepper')),
                ('chicken', models.BooleanField(default=False, verbose_name='chicken')),
                ('basil', models.BooleanField(default=False, verbose_name='basil')),
                ('mushroom', models.BooleanField(default=False, verbose_name='mushroom')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pizza', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
            ],
        ),
    ]
