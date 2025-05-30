# Generated by Django 5.1.5 on 2025-03-01 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0032_alter_extra_caloreis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_branches', models.CharField(max_length=100)),
                ('name_branch_en', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='menu.sitesettings')),
            ],
        ),
    ]
