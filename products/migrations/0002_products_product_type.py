# Generated by Django 3.0.2 on 2022-02-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]