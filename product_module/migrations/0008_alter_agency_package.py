# Generated by Django 4.0.5 on 2022-07-31 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_remove_agency_agency_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.package', verbose_name='atending'),
        ),
    ]
