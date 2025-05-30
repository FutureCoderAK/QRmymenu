# Generated by Django 5.1.5 on 2025-03-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0044_subcategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='caloreis',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name=' (calories)سعرات'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name=' description-(انجليزي) وصف الصنف'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_en',
            field=models.CharField(blank=True, null=True, verbose_name=' description-(انجليزي) وصف الصنف'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='price_offer',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name=' السعر بعد الخصم '),
        ),
    ]
