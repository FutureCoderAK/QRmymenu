from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Color, SiteSettings


@receiver(post_migrate)
def create_default_colors(sender, **kwargs):
    # الحصول على أول إعدادات للموقع أو إنشاء واحد جديد إذا لم يكن موجودًا
    site_settings = SiteSettings.objects.first()
    if not site_settings:
        site_settings = SiteSettings.objects.create()  # يمكنك تخصيص هذا الإنشاء حسب احتياجك

    default_colors = [
        #          bg                      icons text              bg according             text according      
        {"color": "#BFD3C1", "color_name": "#222222", "color_text": "#A5B8A8", "color_price": "#2F4031", "color_cart": "#33FF57"},           
        {"color": "#DDE6ED", "color_name": "#8D6F5A", "color_text": "#B0BCC5", "color_price": "#333333", "color_cart": "#FF5733"},
        {"color": "#EDE0D4", "color_name": "#8D6F5A", "color_text": "#D4C7B0", "color_price": "#361714", "color_cart": "#3357FF"},
        {"color": "#FFFFFF", "color_name": "#555555", "color_text": "#2c3E50", "color_price": "#FFFFFF", "color_cart": "#FF5733"},
        {"color": "darkcyan", "color_name": "#DDDDDD", "color_text": "#006F6F", "color_price": "#F5EAD6", "color_cart": "#FF5733"},
        {"color": "#E8C1B3", "color_name": "#8D6F8A", "color_text": "#D4D7B6", "color_price": "#D4D7B6", "color_cart": "#FFFF33"},
        {"color": "#FF33FF", "color_name": "Pink", "color_text": "#FFFFFF", "color_price": "#FF33FF", "color_cart": "#FF33FF"}
    ]

    for color_data in default_colors:
        Color.objects.get_or_create(site_settings=site_settings, **color_data)