# Generated by Django 5.1.5 on 2025-02-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0026_subcategory_is_hide_subcategory_not_dound'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='price_after',
        ),
    ]
