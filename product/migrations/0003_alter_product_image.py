# Generated by Django 4.1.3 on 2022-12-05 08:40

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_off_percent_product_off_price_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='products/default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 200], upload_to='products'),
        ),
    ]