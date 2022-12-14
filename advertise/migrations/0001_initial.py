# Generated by Django 4.1.3 on 2022-12-07 21:31

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='advertise/default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 200], upload_to='advertise')),
            ],
        ),
    ]
