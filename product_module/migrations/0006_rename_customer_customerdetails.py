# Generated by Django 4.0.5 on 2022-07-26 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_customer_password_customer_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customer',
            new_name='customerDetails',
        ),
    ]
