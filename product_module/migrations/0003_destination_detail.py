# Generated by Django 4.0.4 on 2022-07-25 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_package_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='destination_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_id', models.IntegerField()),
                ('destination', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.package')),
            ],
        ),
    ]
