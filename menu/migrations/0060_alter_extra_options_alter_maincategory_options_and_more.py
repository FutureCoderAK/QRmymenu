# Generated by Django 5.1.7 on 2025-03-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0059_alter_branch_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extra',
            options={'verbose_name_plural': 'extra-اضافات '},
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name_plural': ' Category - صنف رئيسي '},
        ),
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name_plural': 'info-معلومات '},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'dishes-صنف فرعي'},
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='location',
            field=models.URLField(blank=True, help_text='الموقع', null=True, verbose_name='location 📍'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='phone_number',
            field=models.CharField(help_text='رقم التليفون للتواصل', max_length=12, verbose_name='phone number 📞'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url_face',
            field=models.URLField(blank=True, help_text='رابط الفيس', null=True, verbose_name='Facebook link🔵'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url_insta',
            field=models.URLField(blank=True, help_text='رابط الانستجرام', null=True, verbose_name='instegram link📷'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url_tiktok',
            field=models.URLField(blank=True, help_text='رابط التيك توك', null=True, verbose_name='tiktok 🎶'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='url_whats',
            field=models.URLField(blank=True, help_text='رقم الواتساب', null=True, verbose_name='whatsapp 💬'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name=' description (AR)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_en',
            field=models.CharField(blank=True, null=True, verbose_name=' description(EN)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=30, verbose_name='product name(AR) '),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(max_length=30, verbose_name='product name(EN) '),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='uploudImg_SubCategory',
            field=models.ImageField(blank=True, null=True, upload_to='scategory_images/'),
        ),
        migrations.AlterField(
            model_name='workinghours',
            name='close_time',
            field=models.TimeField(blank=True, help_text='close time-وقت الغلق', null=True),
        ),
        migrations.AlterField(
            model_name='workinghours',
            name='open_time',
            field=models.TimeField(blank=True, help_text='open time-وقت الفتح', null=True),
        ),
    ]
