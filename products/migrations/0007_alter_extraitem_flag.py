# Generated by Django 5.0.6 on 2024-07-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraitem',
            name='flag',
            field=models.TextField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending'),
        ),
    ]
