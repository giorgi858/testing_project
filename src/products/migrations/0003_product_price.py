# Generated by Django 5.0 on 2023-12-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=1000),
            preserve_default=False,
        ),
    ]
