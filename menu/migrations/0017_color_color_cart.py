# Generated by Django 5.1.5 on 2025-02-18 18:17

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_remove_color_site_settings_alter_color_color_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_cart',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None),
        ),
    ]
