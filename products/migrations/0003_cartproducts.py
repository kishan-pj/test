# Generated by Django 3.0.2 on 2022-02-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartproducts',
            fields=[
                ('booking_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=50)),
                ('pproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
