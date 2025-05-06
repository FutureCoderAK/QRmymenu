from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('en/', views.en, name='en'),
]
