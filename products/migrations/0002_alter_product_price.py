# Generated by Django 5.0.6 on 2024-06-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
