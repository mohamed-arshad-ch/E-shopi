# Generated by Django 3.1.1 on 2020-09-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.category'),
        ),
    ]
