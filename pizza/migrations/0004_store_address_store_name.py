# Generated by Django 4.2.2 on 2023-07-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]