# Generated by Django 4.0.5 on 2022-07-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=500),
        ),
    ]
