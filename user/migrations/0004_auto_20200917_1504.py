# Generated by Django 3.1.1 on 2020-09-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_product_cname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(default='asdas', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address3',
            field=models.CharField(default='asda', max_length=200),
            preserve_default=False,
        ),
    ]
