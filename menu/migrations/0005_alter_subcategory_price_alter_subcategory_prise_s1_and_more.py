# Generated by Django 5.1.5 on 2025-02-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_subcategory_price_alter_subcategory_prise_s1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='prise_s3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size1',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size2',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='size3',
            field=models.CharField(max_length=5),
        ),
    ]
