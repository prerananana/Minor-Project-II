# Generated by Django 4.0.4 on 2022-08-02 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0008_remove_cartitem_customer_cartitem_user'),
        ('payment_module', '0003_invoicedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_module.package'),
        ),
    ]
