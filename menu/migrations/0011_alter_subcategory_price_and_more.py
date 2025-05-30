# Generated by Django 5.1.5 on 2025-02-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_workinghours_close_period_workinghours_open_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='price_after',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='price_offer',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size1',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size2',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size3',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
