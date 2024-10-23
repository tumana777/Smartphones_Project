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

from core.views import index, contact, smartphones_list, phone_detail, testimonial

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('smartphones/', smartphones_list, name='smartphones_list'),
    path('smartphones/brand=<slug:brand_slug>/', smartphones_list, name='brand_products'),
    path('smartphones/category=<slug:category_slug>/', smartphones_list, name='category_products'),
    path('testimonial/', testimonial, name='testimonial'),
    path('smartphone/<slug:slug>/', phone_detail, name='phone_detail'),
]
