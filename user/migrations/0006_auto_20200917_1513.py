# Generated by Django 3.1.1 on 2020-09-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='cname',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='image',
        ),
    ]
