from django.db import models
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField
from django.contrib.postgres.fields import JSONField
from django import forms
from django.utils.safestring import mark_safe
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
class MainCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name=("Main Category (AR)"),help_text="اسم الصنف الرئيسي (عربي)")  # اسم الصنف الرئيسي
    name_en = models.CharField(max_length=100, verbose_name=(" Main Category (ُEN) "),help_text="(انجليزي)اسم الصنف الرئيسي ")  # اسم الصنف الرئيسي
    uploudImg_Category = models.ImageField(upload_to='category_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ الإنشاء
    class Meta:
        verbose_name_plural = " Category - صنف رئيسي "  
    def __str__(self):
        return self.name
    def clean(self):
        # التحقق إذا كان الاسم بالعربية مكرر
        if MainCategory.objects.filter(name=self.name).exists():
            raise ValidationError(f"الاسم '{self.name}' موجود مسبقًا.")

        # التحقق إذا كان الاسم بالإنجليزية مكرر
        if MainCategory.objects.filter(name_en=self.name_en).exists():
            raise ValidationError(f"الاسم '{self.name_en}' موجود مسبقًا.")

    def save(self, *args, **kwargs):
        self.full_clean()  # يقوم بتنفيذ عملية التحقق قبل الحفظ
        super().save(*args, **kwargs)

# نموذج الفئة الفرعية (Sub Category)

class Extra(models.Model):
    name = models.CharField(max_length=100,verbose_name=("Extra (AR)"),help_text="اسم الاضافه (عربي)")
    name_en = models.CharField(max_length=100,verbose_name=("Extra (EN)"),help_text="اسم الاضافه (انجليزي)")
    caloreis = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True ,help_text="عدد السعرات")
    # استبدال الوصف بحقل لتحميل صورة
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "extra-اضافات "
class Branch(models.Model):
    name_branches = models.CharField(max_length=100)
    name_branch_en = models.CharField(max_length=100)
    url_branch = models.URLField(max_length=200, null=True, blank=True)  # حقل للرابط
    location = models.URLField(max_length=200, null=True, blank=True)  # حقل للرابط
    site_settings = models.ForeignKey('SiteSettings', related_name='branch', on_delete=models.CASCADE)
    def __str__(self):
        return self.name_branches
    class Meta:
        verbose_name_plural = " Branches  🔀 "

class socialmedia(models.Model):
    url_face = models.URLField(max_length=200, null=True, blank=True,verbose_name=("Facebook link🔵"),help_text="رابط الفيس")  # حقل للرابط
    url_insta = models.URLField(max_length=200, null=True, blank=True,verbose_name=("instegram link📷"),help_text="رابط الانستجرام")
    url_whats = models.CharField(max_length=200, null=True, blank=True,verbose_name=("whatsapp 💬"),help_text="رقم الواتساب")
    url_tiktok = models.URLField(max_length=200, null=True, blank=True,verbose_name=("tiktok 🎶"),help_text="رابط التيك توك")
    location = models.URLField(max_length=200, null=True, blank=True,verbose_name=("location 📍"),help_text="الموقع")
    phone_regex = RegexValidator(
        regex=r'^\d{10,15}$', 
        message="رقم الهاتف يجب أن يحتوي فقط على أرقام بدون رموز أو مسافات."
    )
    phone_number = models.CharField(
        max_length=15, 
        validators=[phone_regex], 
        verbose_name="phone number 📞", 
        help_text="رقم التليفون بصيغة صحيحة (بدون رموز أو مسافات)"
    )
    site_settings = models.ForeignKey('SiteSettings', related_name='socialmedia', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.pk and socialmedia.objects.exists():
            raise ValueError("لا يمكن إضافة أكثر من سجل واحد.")
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = " Social 💬 "
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, related_name='subcategories', on_delete=models.CASCADE)
    not_dound = models.BooleanField(default=False)
    is_hide = models.BooleanField(default=False)  # هل اليوم مغلق؟
    uploudImg_SubCategory = models.ImageField(upload_to='scategory_images/', null=True, blank=True)
    name = models.CharField( verbose_name="product name(AR) ",max_length=100)
    name_en = models.CharField(verbose_name="product name(EN) ",max_length=100)
    description = models.CharField(null=True, blank=True,verbose_name=" description (AR)")
    description_en = models.CharField(null=True, blank=True,verbose_name=" description(EN)")
    caloreis = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,verbose_name=" (calories)سعرات")
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,verbose_name="Price - السعر",)
    price_offer = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,verbose_name=" السعر بعد الخصم ")
    size1 = models.CharField(max_length=5, blank=True, null=True)
    prise_s1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    size2 = models.CharField(max_length=5, blank=True, null=True)
    prise_s2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    size3 = models.CharField(max_length=5, blank=True, null=True)
    prise_s3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    extras = models.ManyToManyField(Extra, blank=True, related_name='subcategories', help_text="إضافات متعددة لهذا الصنف.")
     # خيارات متقدمة
    class Meta:
        verbose_name_plural = "dishes-صنف فرعي"
    def product_image(self):
            return mark_safe('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 10px;"/>'.format(self.uploudImg_SubCategory.url))

    
    def clean(self):
        """
        تحقق من صحة البيانات المدخلة.
        """
        # إذا تم إدخال أحجام، يجب إدخال الأسعار المرتبطة بها
        if (self.size1 and not self.prise_s1) or (self.size2 and not self.prise_s2) or (self.size3 and not self.prise_s3):
            raise ValidationError("يجب إدخال السعر المرتبط بالحجم.")

        # إذا تم إدخال أحجام لا يجوز إدخال السعر الأساسي أو سعر الخصم
        if (self.size1 or self.size2 or self.size3):
            # إذا تم إدخال أحجام، لا يتم إدخال السعر الأساسي أو السعر بعد الخصم
            if self.price_offer or self.price:
                raise ValidationError("إذا تم إدخال الأحجام، لا يمكن إدخال السعر الأساسي أو سعر الخصم.")
        else:
            # إذا لم تكن هناك أحجام، يجب إدخال السعر الأساسي أو سعر الخصم
            if not self.price and not self.price:
                raise ValidationError("يجب إدخال السعر الأساسي أو السعر بعد الخصم.")

    def __str__(self):
        return self.name



    
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')
    name = models.CharField(max_length=100,verbose_name=("brand name"),help_text="اسم المطعم")
    desc = models.CharField(max_length=100, blank=True, null=True,verbose_name=("brand description"),help_text="وصف ")
    currencies_choice = [
    ("$", "USD-الدولار الأمريكي"),
    ("€", "EUR-اليورو"),
    ("£", "GBP-الجنيه الإسترليني"),
    ("¥", "JPY-الين الياباني"),
    ("CHF", "CHF-الفرنك السويسري"),
    ("$", "CAD-الدولار الكندي"),
    ("$", "AUD-الدولار الأسترالي"),
    ("¥", "CNY-اليوان الصيني"),
    ("₽", "RUB-الروبيل الروسي"),
    ("SAR", "SAR-الريال السعودي"),
    ("AED", "AED-الدرهم الإماراتي"),
    ("QAR", "QAR-الريال القطري"),
    ("EGP", "EGP-الجنيه المصري"),
    ("OMR", "OMR-الريال العماني"),
    ("₹", "INR-الروبية الهندية"),
    ("₨", "PKR-الروبية الباكستانية"),
    ("$", "MXN-البيزو المكسيكي"),
    ("$", "NZD-الدولار النيوزيلندي"),
    ("kr", "SEK-الكرونة السويدية"),
    ("kr", "DKK-الكرونة الدنماركية"),
    ("RM", "MYR-الرينغيت الماليزي"),
    ("R$", "BRL-الريال البرازيلي"),
    ("$", "ARS-البيزو الأرجنتيني"),
    ("₪", "ILS-الشيكل الإسرائيلي"),
    ("KWD", "KWD-الدينار الكويتي"),
    ("BHD", "BHD-الدينار البحريني"),
    ("Rp", "IDR-الروبية الإندونيسية"),
    ("JOD", "JOD-الدينار الأردني"),
    ("₺", "TRY-الليرة التركية"),
    ("$", "SGD-الدولار السنغافوري")
]
    currencies = models.CharField(max_length=20, choices=  currencies_choice ,verbose_name=("currencies"),help_text="العمله")
    def __str__(self):
        return "Site Settings"
    
    def save(self, *args, **kwargs):
    # التأكد من أن هناك سجل واحد فقط في SiteSettings
        if not SiteSettings.objects.exists():  # إذا لم يكن هناك أي سجل
            super().save(*args, **kwargs)  # حفظ السجل الأول
        else:
        # إذا كان السجل موجودًا، قم بتحديثه بدلاً من رفع استثناء
            existing_record = SiteSettings.objects.first()  # الحصول على السجل الأول
            self.id = existing_record.id  # تعيين الـ id للسجل الحالي
            super().save(*args, **kwargs)  # حفظ التعديلات على السجل الموجود
    
    class Meta:
        verbose_name_plural = "info-معلومات "

SITE_CHOICES = [
        ('all', 'All days-كل الايام'),
        ('Sat', 'Sat-السبت'),
        ('Sun', 'Sun-الاحد'),
        ('Mon', 'Mon-الاثنين'),
        ('Tue', 'Tue-الثلاثاء'),
        ('Wed', 'Wed-الاربعاء'),
        ('Thu', 'Thu-الخميس'),
        ('Fri', 'Fri-الجمعه'),
    ]
class WorkingHours(models.Model):
    days = MultiSelectField(choices=SITE_CHOICES, blank=True)

    
    AM_or_PM = [
        ('AM', 'AM-صباحا'),
        ('PM', 'PM-مساءا'),
    ]

    site_settings = models.ForeignKey('SiteSettings', related_name='working_hours', on_delete=models.CASCADE)  # علاقة مع SiteSettings
    
    # إضافة حقل AM/PM للفترات
    open_time = models.TimeField(null=True, blank=True,help_text="open time-وقت الفتح")  # وقت الفتح
    open_period = models.CharField(max_length=2, choices=AM_or_PM, default='AM')  # فترة فتح المحل
    close_time = models.TimeField(null=True, blank=True,help_text="close time-وقت الغلق")  # وقت الإغلاق
    close_period = models.CharField(max_length=2, choices=AM_or_PM, default='PM')  # فترة إغلاق المحل
    
    is_closed = models.BooleanField(default=False)  
    is_open_24h = models.BooleanField(default=False, verbose_name="٢٤ ساعة")
    def get_days(self):
        return self.days.split(',') if isinstance(self.days, str) else self.days
    def clean(self):
        if self.is_closed and self.is_open_24h:
            raise ValidationError(f" ❌'closed'و '24  ساعه ' لا يمكن اختيار ")
    def save(self, *args, **kwargs):
        self.full_clean()  # يقوم بتنفيذ عملية التحقق قبل الحفظ
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = " hour 🕓  "

class Slider(models.Model):
    site_settings = models.ForeignKey(SiteSettings, related_name='sliders', on_delete=models.CASCADE)  # ربط بـ SiteSettings
    image = models.ImageField(upload_to='sliders/')  # صورة الـ Slider فقط
    class Meta:
        verbose_name_plural = "  Slider  🔁  "
    def __str__(self):
        return f"Slider {self.id}"  # يمكن عرض معرف الـ Slider
    
    
class Color(models.Model):
    site_settings = models.ForeignKey(SiteSettings, related_name='colors', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    # استبدال ColorField بـ CharField لتخزين اللون كـ HEX
    color = models.CharField(max_length=100, default='#FFFFFF')  # الحقل الذي يخزن اللون
    color_name = models.CharField(max_length=100, default='#FFFFFF')
    color_text = models.CharField(max_length=100, default='#000000')
    color_price = models.CharField(max_length=100, default='#FF5733')
    color_cart = models.CharField(max_length=100, default='#FF5733')
    
    class Meta:
        # التأكد من أن هناك لون واحد فقط مفعّل في نفس الوقت
        constraints = [
            models.UniqueConstraint(fields=['is_active'], condition=models.Q(is_active=True), name='يجب اختيار لون واحد فقط')
        ]
        verbose_name_plural = " Color 🎨  "
    def __str__(self):
        return self.color
    
    # class Meta:
    #     

      