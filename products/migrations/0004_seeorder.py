# Generated by Django 3.0.2 on 2022-02-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cartproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeorder',
            fields=[
                ('product_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.CharField(max_length=100)),
                ('product_type', models.CharField(blank=True, max_length=100)),
                ('product_image', models.FileField(upload_to='product_images')),
            ],
            options={
                'db_table': 'seeorder',
            },
        ),
    ]
