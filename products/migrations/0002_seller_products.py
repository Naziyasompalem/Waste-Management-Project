# Generated by Django 5.0.6 on 2024-07-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Products',
            field=models.ManyToManyField(blank=True, related_name='Sellers', to='products.product'),
        ),
    ]
