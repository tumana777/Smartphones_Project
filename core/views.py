from django.shortcuts import render
from .models import Smartphone, Brand
from django.core.paginator import Paginator

def index(request):

    return render(request, 'index.html')

def smartphones_list(request):

    brands = get_brands_with_products_count()

    smartphones = Smartphone.objects.select_related('brand').all()

    paginator = Paginator(smartphones, 9)
    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    context = {
        'brands': brands,
        'smartphones': smartphones,
    }

    return render(request, 'shop.html', context)

def brand_products(request, slug):

    brands = get_brands_with_products_count()

    brand = Brand.objects.get(slug=slug)

    smartphones = Smartphone.objects.select_related('brand').filter(brand=brand)

    paginator = Paginator(smartphones, 9)
    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    context = {
        'brands': brands,
        'smartphones': smartphones
    }

    return render(request, 'brand_products.html', context)

def phone_detail(request, slug):

    brands = get_brands_with_products_count()

    smartphone = Smartphone.objects.select_related('brand').get(slug=slug)

    context = {
        'smartphone': smartphone,
        'brands': brands,
    }

    return render(request, 'phone-detail.html', context)

def contact(request):

    return render(request, 'contact.html')

def testimonial(request):

    return render(request, 'testimonial.html')

def get_brands_with_products_count():

    brands = Brand.objects.all()

    for brand in brands:
        model = Smartphone.objects.filter(brand=brand)
        model_count = model.count()
        brand.model_count = model_count

    return brands