from django.db import models
from django.contrib import admin
from .models import MainCategory,SubCategory,SiteSettings, WorkingHours, Slider,Color,Extra,Branch,SITE_CHOICES,socialmedia
from django import forms
from .models import Color
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from import_export.widgets import Widget
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.utils.safestring import mark_safe
from .widgets import DisabledChoicesSelectMultiple  # أو حسب مكان الكلاس
from django.forms.models import BaseInlineFormSet
from import_export import resources, fields
from import_export.admin import ExportMixin, ImportExportModelAdmin
from import_export.formats.base_formats import CSV, XLSX
from .import_export_patch import PatchedModelResource
from django.forms import Select
from django.forms.widgets import ClearableFileInput
import openai
import os

# openai.api_key = os.getenv("OPENAI_API_KEY")
class SubCategoryResource(PatchedModelResource):
    main_category = fields.Field(
        column_name='main_category',
        attribute='main_category',
        widget=ForeignKeyWidget(MainCategory, 'name_en')  # تأكد إنك بتستخدم اسم صحيح للتصنيف
    )

    extras = fields.Field(
        column_name='extras',
        attribute='extras',
        widget=ManyToManyWidget(Extra, field='name', separator=',')
    )

    class Meta:
        model = SubCategory
        skip_admin_log = True
        import_id_fields = ('name_en',)  # أو أي حقل يكون مميز
        fields = (
            'main_category', 'not_found', 'is_hide', 'uploudImg_SubCategory',
            'name', 'name_en', 'description', 'description_en', 'caloreis', 'price',
            'price_offer', 'size1', 'prise_s1', 'size2', 'prise_s2',
            'size3', 'prise_s3', 'extras'
        )


class SubCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30, 'class': 'form-control', 'style': 'width: 250px;'}),
            'name_en': forms.TextInput(attrs={'size': 30, 'class': 'form-control', 'style': 'width: 250px;'}),
            'description': forms.TextInput(attrs={'size': 30, 'class': 'form-control', 'style': 'width: 100%;'}),
            'description_en': forms.TextInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 100%;', 'placeholder': ''}),
            
            'caloreis': forms.NumberInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'max-width: 70%;', 'placeholder': 'عدد السعرات'}),
            # 'price': forms.NumberInput(attrs={
            #     'size': 30, 'class': 'form-control', 'style': 'max-width: 70%;',}),
            'price_offer': forms.NumberInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;',}),
            'size1': forms.TextInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': 'L'}),
            'prise_s1': forms.NumberInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': '40'}),
            'size2': forms.TextInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': 'M'}),
            'prise_s2': forms.NumberInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': '50'}),
            'size3': forms.TextInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': 'D'}),
            'prise_s3': forms.NumberInput(attrs={
                'size': 30, 'class': 'form-control', 'style': 'width: 70px;', 'placeholder': '100'}),
        }

            
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['main_category'].help_text = 'الصنف الرئيسي الذي يتبع له هذا المنتج.'
        self.fields['name'].help_text = 'اسم المنتج باللغة العربية.'
        self.fields['name_en'].help_text = 'اسم المنتج باللغة الإنجليزية.'
        self.fields['description'].help_text = 'وصف المنتج باللغة العربية.'
        self.fields['description_en'].help_text = 'وصف المنتج باللغة الإنجليزية.'
        self.fields['caloreis'].help_text = 'عدد السعرات الحرارية في المنتج.'
        self.fields['price'].help_text = 'السعر الأساسي للمنتج.'
        self.fields['price_offer'].help_text = 'السعر بعد الخصم (اختياري).'
        self.fields['uploudImg_SubCategory'].help_text = 'صورة توضيحية للمنتج.'
        self.fields['extras'].help_text = 'الإضافات أو الخيارات المرتبطة بهذا المنتج.'
        self.fields['not_dound'].help_text = 'هل المنتج غير متوفر حاليًا؟'
        self.fields['is_hide'].help_text = 'إخفاء المنتج من الظهور للعملاء.'
        self.fields['size1'].help_text = 'الحجم الأول .'
        self.fields['prise_s1'].help_text = 'سعر الحجم الأول .'
        self.fields['size2'].help_text = 'الحجم الثاني .'
        self.fields['prise_s2'].help_text = 'سعر الحجم الثاني.'
        self.fields['size3'].help_text = 'الحجم الثالث .'
        self.fields['prise_s3'].help_text = 'سعر الحجم الثالث .'

    

        # 🏷️ تعيين labels مخصصة لكل حقل
        self.fields['main_category'].label = 'Main'
        self.fields['size1'].label = ''
        self.fields['prise_s1'].label = ''
        self.fields['size2'].label = ''
        self.fields['prise_s2'].label = ''
        self.fields['size3'].label = ''
        self.fields['prise_s3'].label = ''
        self.fields['not_dound'].label = 'not available'
        self.fields['is_hide'].label = ' hide '

class SubCategoryAdmin(ImportExportModelAdmin):
    form = SubCategoryAdminForm
    resource_class = SubCategoryResource
    save_on_top = True

    formats = (CSV, XLSX) 
    
    list_display = ('main_category', 'name','name_en', 'price', 'price_offer','image_tag')
    fieldsets = (
        ('📌 بيانات أساسية', {
            'fields': (
                'main_category',
                'name',
                'name_en',
                'uploudImg_SubCategory',
                'price',
                'price_offer',
                'extras',
        ),
        }),
        ('تفاصيل', {
            'fields': (
                'description',
                'description_en',
                'caloreis',

                ),
            
        }),
        ('📏 الأحجام والأسعار', {
            'fields': (
                ('size1', 'prise_s1'),
                ('size2', 'prise_s2'),
                ('size3', 'prise_s3'),
            ),
            'classes': ('collapse',),  # يفتحها عند الحاجة
        }),
        ('⚙️ إعدادات أخرى', {
            'fields': ('not_dound', 'is_hide'),
        }),
    )
    
    search_fields = ('name', 'name_en')
    list_filter = ('main_category', 'is_hide')
    readonly_fields = ('product_image',)
    ordering = ['-created_at']
    def uploudImg_SubCategory_thumbnail(self, obj):
        if obj.uploudImg_SubCategory:
            return format_html('<img src="{}" style="width: 50px; height: 50px ;"/>', obj.uploudImg_SubCategory.url)
        return "No image"
    uploudImg_SubCategory_thumbnail.short_description = 'Image'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # إضافة بعض التعليمات لتخصيص الـ widget إذا كان ذلك ضروريًا
        if hasattr(self, 'instance') and self.instance and self.instance.uploudImg_SubCategory:
            self.fields['uploudImg_SubCategory'].widget.attrs['style'] = 'display: none;'  # إخفاء حقل الصورة

    def image_tag(self, obj):
        if obj.uploudImg_SubCategory:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 10px;" />', obj.uploudImg_SubCategory.url)
        return "-"
    image_tag.short_description = "الصورة"


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = socialmedia
        fields = '__all__'
        widgets = {
            'url_face': forms.URLInput(attrs={'size': 30,'class': 'form-control','style': 'width: 100%;', }),
            'url_insta': forms.URLInput(attrs={'size': 30,'class': 'form-control','style': 'width: 100%;', }),
            'url_whats': forms.URLInput(attrs={'size': 30,'class': 'form-control','style': 'width: 100%;', }),
            'url_tiktok': forms.URLInput(attrs={'size': 30,'class': 'form-control','style': 'width: 100%;', }),
            'location': forms.URLInput(attrs={'size': 30,'class': 'form-control','style': 'width: 100%;','placeholder':'فرع مدينه نصر', }),
            'phone_number': forms.TextInput(attrs={'size': 30,'class': 'form-control','style': 'max-width: 70%;','placeholder':'رمز الدوله + رقم التليفون', }),
            
        }
class socialmediaAdmin(admin.ModelAdmin):
    list_display = ['url_face','url_insta','url_whats','url_tiktok','location','phone_number']   
    def colored_url_whats(self, obj):
        if obj.url_whats:
            return format_html('<span style="color: #25D366;">رابط موجود</span>')
        else:
            return format_html('<span style="color: gray;">لا يوجد</span>')
    colored_url_whats.short_description = "واتساب"
    
class socialmediaInline(admin.StackedInline):  # أو StackedInline لو حابب
    model = socialmedia
    form = SocialMediaForm
    extra = 0
    def has_add_permission(self, request, obj=None):
        if socialmedia.objects.exists():
            return False
        return True
     
class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30, 'placeholder': '  مثلا: صوص ابيض','class': 'form-control','dir': 'rtl'
                                            ,'style': 'width: 220px;', 
                                           
                                           }),
            'name_en': forms.TextInput(attrs={'size': 40, 'placeholder': 'example: white sose', 'class': 'form-control',
                                              'style': 'width: 220px;',
                                              }),
            'caloreis': forms.NumberInput(attrs={'size': 40, 'placeholder': 'kcal:سعرات', 'class': 'form-control',
                                              'style': 'width: 220px;',
                                              }),
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if self.instance.pk is None and Extra.objects.filter(name=name).exists():
            raise ValidationError("هذا الاسم موجود بالفعل.")
        return name
    
    def clean_name_en(self):
        name_en = self.cleaned_data['name_en']
        if self.instance.pk is None and Extra.objects.filter(name_en=name_en).exists():
            raise ValidationError("هذا الاضافه موجوده بالفعل.")
        return name_en
        
class ExtraAdmin(admin.ModelAdmin):
    form = ExtraForm
    list_display = ['name','name_en','caloreis', 'price']
    search_fields = ['name']
    list_filter = ['price']
    

# تخصيص مظهر الفئة الرئيسية في صفحة الإدمن
class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = MainCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30, 'placeholder': 'اسم الصنف الرئيسي','class': 'form-control','dir': 'rtl'
                                            ,'style': 'width: 220px;', 
                                           
                                           }),
            'name_en': forms.TextInput(attrs={'size': 40, 'placeholder': 'Main Category Name', 'class': 'form-control',
                                              'style': 'width: 220px;',
                                              }),
           'uploudImg_Category': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
                'title': 'اختر صورة',
          
    }),
        }
    
        
class MainCategoryAdmin(admin.ModelAdmin):
    # inlines = [SubCategoryInline]
    form = MainCategoryForm
    list_display = ('name','name_en','image', 'created_at')  # عرض اسم الفئة وتاريخ الإنشاء في قائمة الفئات الرئيسية
    fieldsets = (
        (None, {
            'fields': ('name', 'name_en', 'uploudImg_Category','image_tag'),
            'description': " صنف رئيسي- Main Category"
        }),
    )
    readonly_fields = ('image_tag',)
    search_fields = ('name',)  # إضافة إمكانية البحث حسب اسم الفئة الرئيسية
    list_filter = ('created_at',)  # تصنيف الفئات حسب تاريخ الإنشاء
    def image_tag(self, obj):
        if obj.uploudImg_Category:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 10px;" />', obj.uploudImg_Category.url)
        return "هنا تظهر الصورة بعد الحفظ، وكذلك عند تعديل المنتج."
    image_tag.short_description = "image"
    def image(self, obj):
        if obj.uploudImg_Category:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 10px;" />', obj.uploudImg_Category.url)
        return "هنا تظهر الصورة بعد الحفظ، وكذلك عند تعديل المنتج."
    image.short_description = "image"
    
    
    


class WorkingHoursForm(forms.ModelForm):
    
    class Meta:
        model = WorkingHours
        fields = '__all__'
        widgets = {
            'open_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'وقت الفتح - مثال: 08:00',
                'style': 'width: 100px;',
            }),
            'close_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'وقت الإغلاق - مثال: 11:00',
                'style': 'width: 100px; color: red;',
            }),
            'close_period': forms.Select(attrs={
                'style': 'width: 100px; color: red;',
                'class': 'form-control',
                
            }),
            'open_period': forms.Select(attrs={
                'style': 'color: green;',
            }),
        }
        labels = {
            'open_time': '',
            'close_time': '',
            'is_closed': '',
            'is_open_24h': '',
            'open_period':'',
            'close_period':'',
        }
        help_texts = {
            'is_closed': 'Closed | مغلق',
            'is_open_24h': 'Throughout the day | مدار اليوم',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # كل الأيام اللي مختارة في سجلات تانية
        used_days = WorkingHours.objects.exclude(
            pk=self.instance.pk if self.instance.pk else None
        ).values_list('days', flat=True)

        # دي هتبقى قائمة بالقيم زي: ['Sat', 'Sun', 'Mon', ...]
        all_used = set()
        for entry in used_days:
            if isinstance(entry, list):
                all_used.update(entry)
            elif isinstance(entry, str):
                all_used.update(entry.split(','))
        
        # widget مخصص بيعطل الأيام المستخدمة
        self.fields['days'] = forms.MultipleChoiceField(
            choices=SITE_CHOICES,
            required=False,
            label="اختيار الأيام",
            widget=DisabledChoicesSelectMultiple(disabled_choices=all_used)
        )
    def clean_days(self):
        selected_days = self.cleaned_data.get('days', [])

        # ✅ لا يمكن اختيار "all" مع أيام أخرى
        if 'all' in selected_days and len(selected_days) > 1:
            raise forms.ValidationError("لا يمكن اختيار 'كل الأيام' مع أيام أخرى.")

        # ✅ لا يمكن تكرار 'all' في أكثر من سجل
        existing = WorkingHours.objects.exclude(
            pk=self.instance.pk if self.instance.pk else None
        )

        for obj in existing:
            existing_days = obj.days or []
            if 'all' in existing_days and 'all' in selected_days:
                raise forms.ValidationError("يوجد سجل آخر يحتوي على 'كل الأيام' بالفعل، لا يمكن تكراره.")

        # ✅ لا يمكن تكرار أي يوم عادي (سبت، أحد، ...الخ)
        used_days = set()
        for obj in existing:
            if isinstance(obj.days, str):
                used_days.update(obj.days.split(','))
            elif isinstance(obj.days, list):
                used_days.update(obj.days)

        duplicated_days = used_days.intersection(selected_days)
        if duplicated_days:
            readable = ', '.join(dict(SITE_CHOICES).get(day, day) for day in duplicated_days)
            raise forms.ValidationError(f"اليوم/الأيام التالية مستخدمة بالفعل: {readable}")

        # ✅ لا يمكن اختيار 'all' إذا كان هناك أيام جزئية مستخدمة في سجلات أخرى
        if 'all' in selected_days:
            for obj in existing:
                existing_days = obj.days or []
                if isinstance(existing_days, str):
                    existing_days = existing_days.split(',')

                if any(day != 'all' for day in existing_days):
                    raise forms.ValidationError("لا يمكن اختيار 'كل الأيام' لأن هناك سجلات تحتوي على أيام جزئية بالفعل.")

        return selected_days

    
        
class WorkingHoursFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        all_selected_days = []

        for form in self.forms:
            if form.cleaned_data.get('DELETE', False):
                continue

            days = form.cleaned_data.get('days', [])
            if not days:
                continue

            for day in days:
                if day in all_selected_days:
                    raise ValidationError(f"اليوم '{day}' مكرر في أكثر من سجل. يرجى تعديله.")
                all_selected_days.append(day)
class WorkingHoursInline(admin.StackedInline):  # أو TabularInline لو تحب
    model = WorkingHours
    form = WorkingHoursForm
    formset = WorkingHoursFormSet
    # formset = WorkingHoursFormSet
    extra = 0
    fieldsets = [
        ('🕓 ساعات العمل', {
            'fields': [
                'days',
                ('open_time', 'open_period'),     # جنب بعض
                ('close_time', 'close_period'),   # جنب بعض
                ('is_closed', 'is_open_24h'),  
                   
            ],
            'description': " نف رئيسي- Main Category"   # جنب بعض
        }),
    ]
    formfield_overrides = {
        models.TimeField: {'widget': forms.TimeInput(format='%H:%M')},
        models.CharField: {'widget': Select(attrs={
            'style': 'color: green;',
        })}
    }
    def has_add_permission(self, request, obj=None):
        for instance in WorkingHours.objects.all():
            # التحقق من وجود "all" في الأيام
            if 'all' in instance.get_days():
                return False
        return super().has_add_permission(request, obj)
    
class WorkingHoursAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/workinghours_admin.js',)  # مسار ملف JS اللي هتعمله
    formfield_overrides = {
        forms.MultipleChoiceField: {'widget': Select(attrs={
            'style': 'color: green;',
        })}
    }
    form = WorkingHoursForm
    













class IconImageUploadWidget(ClearableFileInput):
    def format_value(self, value):
        return ""

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # نخفي القيمة الحالية (currently) نهائيًا
        context['widget']['is_initial'] = False
        return context

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs["style"] = "display: none;"
        input_html = super().render(name, value, attrs, renderer)
        return format_html(
            '''
            <label style="
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                padding: 10px 14px;
                background-color: #007bff;
                color: white;
                border-radius: 50%;
                cursor: pointer;
                font-weight: 500;
                font-size: 14px;
                transition: background-color 0.3s ease;
            " onmouseover="this.style.backgroundColor='#0056b3'"
              onmouseout="this.style.backgroundColor='#007bff'">
                <svg xmlns="http://www.w3.org/2000/svg" 
                    width="20" height="20" viewBox="0 0 24 24" 
                    fill="currentColor">
                    <path d="M5 20h14v-2H5v2zm7-14l-5 5h3v4h4v-4h3l-5-5z"/>
                </svg>
                {input}
            </label>
            ''',
            input=input_html
        )

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'
        widgets = {
            'image': IconImageUploadWidget,
        
        }
        labels = {
            'image': '',
        }
class SliderInline(admin.StackedInline):  # أو TabularInline حسب استخدامك
    model = Slider
    form = SliderForm
    extra = 1
    readonly_fields = ['custom_note','image_preview']  # ضروري
    # fields = ['image_preview', 'image'] 
     # الصورة ثم زر الرفع
    fieldsets = [
        ('', {
            'fields': [
                'custom_note',
                ('image_preview', 'image'),     # جنب بعض
            ],
            'description': " نف رئيسي- Main Category"   # جنب بعض
        }),
    ]
    def custom_note(self, obj):
        return format_html(
            '<div style="padding: 10px; background-color: #f8f9fa; border: 1px solid #ddd; border-radius: 6px; margin-bottom: 10px;">'
            '<strong>ملاحظة:</strong>  يتم عرض الصوره بعد الحفظ.'
            '</div>'
        )

    custom_note.short_description = ""  # عشان ما يطلعش عنوان فوقه
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="150" style="border-radius:8px;"style="border-radius:50%; object-fit:cover; border: 1px solid #ccc;" />', obj.image.url)
        return "No image uploaded"
    image_preview.short_description = ""
    

class SliderAdmin(admin.ModelAdmin):
    form = SliderForm
    fields = ['image']  # عرض حقل الصورة فقط
    list_display = ['image']  # عرض الصورة في واجهة الإدارة


class ColorInlineForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
            'color_name': forms.TextInput(attrs={'type': 'color'}),
            'color_text': forms.TextInput(attrs={'type': 'color'}),
            'color_price': forms.TextInput(attrs={'type': 'color'}),
            'color_cart': forms.TextInput(attrs={'type': 'color'}),
        }
class ColorInline(admin.TabularInline):  # أو StackedInline لو حابب
    model = Color
    form = ColorInlineForm
    extra = 0
  

    
class SiteSettingsInline(admin.StackedInline):  
    model = SiteSettings
    extra = 0 # تحديد عدد الإدخالات الفارغة الإضافية
    max_num = 1
    can_delete = False
    

class BranchInline(admin.StackedInline):  # يمكنك استخدام StackedInline إذا كنت تفضل عرض الحقول بشكل عمودي
    model = Branch
    extra = 1  # عدد الفروع الإضافية الفارغة التي ستظهر عند التحرير



class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30, 'placeholder': 'اسم البراند','class': 'form-control'
                                            ,'style': 'width: 220px;', 
                                
                                           }),
            'desc': forms.TextInput(attrs={'size': 40, 'placeholder': 'وصف او شعار للمطعم', 'class': 'form-control',
                                              'style': 'width: 220px;',
                                              }),
           'logo': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
                'title': 'logo',
          
    }),
        }
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    fieldsets = (
    ('info 🧠', {
        'fields': ('image_logo','logo', 'name', 'desc','currencies'),
        'description': " General Settings  |   الاعدادات العامه"
    }),
)
    list_display = ('name','desc','image_logo_td','currencies')
    inlines = [WorkingHoursInline,socialmediaInline,SliderInline,ColorInline,BranchInline] # دمج روابط السوشيال ميديا داخل إعدادات الموقع
    search_fields = ('name','desc')
    readonly_fields = ('image_logo',)
    def image_logo(self, obj):
        if obj.logo:  # تأكد من الحقل الصحيح هنا
            return format_html('<img src="{}" width="80" height="80" style="display: block; margin: auto; object-fit: cover; border-radius: 10px;" />', obj.logo.url)
        return "هنا تظهر الصورة بعد الحفظ، وكذلك عند تعديل المنتج."
    image_logo.short_description = "-"

    def image_logo_td(self, obj):
        if obj.logo:  # تأكد من الحقل الصحيح هنا
            return format_html('<img src="{}" width="40" height="40" style="object-fit: cover; border-radius: 10px;" />', obj.logo.url)
        return "هنا تظهر الصورة بعد الحفظ، وكذلك عند تعديل المنتج."
    image_logo_td.short_description = "logo"

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False  
        return True  

    # منع الحذف
    def has_delete_permission(self, request, obj=None):
        if SiteSettings.objects.count() <= 1:
            return True 
        return False 





admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Extra,ExtraAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)




