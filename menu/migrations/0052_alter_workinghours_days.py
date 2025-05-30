# Generated by Django 5.1.7 on 2025-03-12 12:09

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0051_remove_workinghours_day_workinghours_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinghours',
            name='days',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('all', 'All days-كل الايام'), ('Sat', 'Sat-السبت'), ('Sun', 'Sun-الاحد'), ('Mon', 'Mon-الاثنين'), ('Tue', 'Tue-الثلاثاء'), ('Wed', 'Wed-الاربعاء'), ('Thu', 'Thu-الخميس'), ('Fri', 'Fri-الجمعه')], max_length=31),
        ),
    ]
