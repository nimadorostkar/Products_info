# Generated by Django 4.1.3 on 2022-11-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='off_percent',
            field=models.CharField(default=0, max_length=256),
        ),
        migrations.AddField(
            model_name='product',
            name='off_price',
            field=models.CharField(default=0, max_length=256),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=0, max_length=256),
        ),
    ]
