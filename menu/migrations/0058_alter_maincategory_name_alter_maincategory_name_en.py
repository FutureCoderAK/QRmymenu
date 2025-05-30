# Generated by Django 5.1.7 on 2025-03-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0057_alter_color_color_alter_color_color_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='name',
            field=models.CharField(help_text='اسم الصنف الرئيسي (عربي)', max_length=100, verbose_name='Main Category (AR)'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='name_en',
            field=models.CharField(help_text='(انجليزي)اسم الصنف الرئيسي ', max_length=100, verbose_name=' Main Category (ُEN) '),
        ),
    ]
