# Generated by Django 4.0.5 on 2022-07-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_package_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', max_length=500)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('subject', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
