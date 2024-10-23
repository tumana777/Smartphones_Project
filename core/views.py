from django.db.models import Q
from django.shortcuts import render
from .models import Smartphone, Brand
from django.core.paginator import Paginator

def index(request):

    return render(request, 'index.html')

def smartphones_list(request):

    brands = get_brands_with_products_count()

    search_query = request.GET.get('q')

    if search_query:
        smartphones = Smartphone.objects.select_related('brand').filter(name__icontains=search_query)
    else:
        smartphones = Smartphone.objects.select_related('brand').all()

    total_smartphones = smartphones.count()

    paginator = Paginator(smartphones, 9)
    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    context = {
        'total': total_smartphones,
        'search_query': search_query,
        'brands': brands,
        'smartphones': smartphones,
    }

    return render(request, 'shop.html', context)

def brand_products(request, slug):

    brands = get_brands_with_products_count()

    brand = Brand.objects.get(slug=slug)

    search_query = request.GET.get('q')

    if search_query:
        smartphones = Smartphone.objects.select_related('brand').filter(Q(name__icontains=search_query) & Q(brand=brand))
    else:
        smartphones = Smartphone.objects.select_related('brand').filter(brand=brand)

    total_smartphones = smartphones.count()

    paginator = Paginator(smartphones, 9)
    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    context = {
        'total': total_smartphones,
        'search_query': search_query,
        'brands': brands,
        'smartphones': smartphones
    }

    return render(request, 'shop.html', context)

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