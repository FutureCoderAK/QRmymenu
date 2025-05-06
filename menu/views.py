from django.shortcuts import render
from django.db.models import Prefetch
from .models import MainCategory,SiteSettings,Slider,WorkingHours,Color,SubCategory,Branch,socialmedia
def menu(request):
        subcategories_qs = SubCategory.objects.filter(is_hide=False).select_related('main_category')
        main_categories = MainCategory.objects.prefetch_related(Prefetch('subcategories', queryset=subcategories_qs)).all()
        site_settings = SiteSettings.objects.all()
        slider_images = Slider.objects.all()
        hours = WorkingHours.objects.all()
        background_color = Color.objects.all()
        branches = Branch.objects.all()
        colors = Color.objects.filter(is_active=True)
        social_media = socialmedia.objects.all()
        return render(request, 'base.html', {
            'main_categories': main_categories,
            'site_settings': site_settings,
            'Slider_img': slider_images,
            'hours': hours,
            'background_color': background_color,
            'branches' : branches ,
            'colors': colors,
            'social_media': social_media,
        })

def en(request):
    subcategories_qs = SubCategory.objects.filter(is_hide=False).select_related('main_category')
    main_categories = MainCategory.objects.prefetch_related(Prefetch('subcategories', queryset=subcategories_qs)).all()
    site_settings = SiteSettings.objects.all()
    slider_images = Slider.objects.all()
    hours = WorkingHours.objects.all()
    colors = Color.objects.filter(is_active=True)
    branches = Branch.objects.all()
    return render(request, 'index-en.html',{
        'main_categories': main_categories,
            'site_settings': site_settings,
            'Slider_img': slider_images,
            'hours': hours,
            'colors': colors,
            'branches' : branches ,
    })