# Generated by Django 5.1.5 on 2025-03-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0035_rename_url_branch_url_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
