# Generated by Django 3.1.1 on 2020-09-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_wishlist_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
