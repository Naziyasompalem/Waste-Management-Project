# Generated by Django 5.0.6 on 2024-07-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_shippinginformation_alter_seller_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
