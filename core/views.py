from django.shortcuts import render
from .models import Smartphone, Brand

def index(request):

    return render(request, 'index.html')

def smartphones_list(request):

    brands = Brand.objects.all()

    for brand in brands:
        model = Smartphone.objects.filter(brand=brand)
        model_count = model.count()
        brand.model_count = model_count

    smartphones = Smartphone.objects.select_related('brand').all()

    context = {'brands': brands, 'smartphones': smartphones}

    return render(request, 'shop.html', context)

def brand_products(request, slug):

    brands = Brand.objects.all()

    for brand in brands:
        model = Smartphone.objects.filter(brand=brand)
        model_count = model.count()
        brand.model_count = model_count

    brand = Brand.objects.get(slug=slug)

    smartphones = Smartphone.objects.prefetch_related('brand').filter(brand=brand)

    context = {
        'brands': brands,
        'smartphones': smartphones
    }

    return render(request, 'brand_products.html', context)

def phone_detail(request, slug):

    brands = Brand.objects.all()

    for brand in brands:
        model = Smartphone.objects.filter(brand=brand)
        model_count = model.count()
        brand.model_count = model_count

    smartphone = Smartphone.objects.prefetch_related('brand').get(slug=slug)

    context = {
        'smartphone': smartphone,
        'brands': brands,
    }

    return render(request, 'phone-detail.html', context)

def contact(request):

    return render(request, 'contact.html')

def testimonial(request):

    return render(request, 'testimonial.html')