"""
URL configuration for E_commerce_web_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from core.views import SmartphonesListView, PhoneDetailView, smartphones_list

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('testimonial/', TemplateView.as_view(template_name='testimonial.html'), name='testimonial'),
    path('smartphones/', SmartphonesListView.as_view(), name='smartphones_list'),
    path('smartphones/brand=<slug:brand_slug>/', SmartphonesListView.as_view(), name='brand_products'),
    path('smartphones/category=<slug:category_slug>/', SmartphonesListView.as_view(), name='category_products'),
    path('smartphone/<slug:slug>/', PhoneDetailView.as_view(), name='phone_detail'),
]
