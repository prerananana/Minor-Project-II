# Generated by Django 4.0.4 on 2022-08-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_package_package_name_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('entered_on', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.customer')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.package')),
            ],
        ),
    ]
