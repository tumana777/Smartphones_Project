from django.shortcuts import render
from .models import Smartphone, Brand, Category, ProductTag
from django.core.paginator import Paginator

def index(request):

    return render(request, 'index.html')

def smartphones_list(request, category_slug=None, brand_slug=None):

    categories = Category.objects.filter(parent=None)

    for category in categories:
        all_categories = category.get_descendants(include_self=True)
        model_count = Smartphone.objects.filter(category__in=all_categories).count()
        category.model_count = model_count

    brands = get_brands_with_products_count()

    search_query = request.GET.get('q')
    price_query = request.GET.get('rangeInput')
    tag_query = request.GET.get('tag-name')
    sort_by = request.GET.get('sort_by', '-created_at')

    smartphones = Smartphone.objects.all()

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        all_categories = category.get_descendants(include_self=True)
        smartphones = smartphones.filter(category__in=all_categories)
        categories = Category.objects.filter(parent=category)

    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        smartphones = smartphones.filter(brand=brand)

    if search_query:
        smartphones = smartphones.filter(name__icontains=search_query)

    if price_query:
        smartphones = smartphones.filter(price__lte=price_query)

    if tag_query:
        smartphones = smartphones.filter(tags__name=tag_query)

    smartphones = smartphones.order_by(sort_by)

    smartphones = smartphones.prefetch_related('category').select_related('brand').prefetch_related('tags')

    total_smartphones = smartphones.count()

    tags = ProductTag.objects.all()

    paginator = Paginator(smartphones, 9)
    page_number = request.GET.get('page')
    smartphones = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    querystring = query_params.urlencode()

    context = {
        'categories': categories,
        'total': total_smartphones,
        'search_query': search_query,
        'brands': brands,
        'smartphones': smartphones,
        'querystring': querystring,
        'tags': tags,
    }

    return render(request, 'shop.html', context)

def phone_detail(request, slug):

    brands = get_brands_with_products_count()

    smartphone = Smartphone.objects.select_related('brand').get(slug=slug)

    brand = Brand.objects.get(id=smartphone.brand_id)

    smartphones = Smartphone.objects.filter(brand=brand).select_related('brand')

    context = {
        'smartphone': smartphone,
        'brands': brands,
        'smartphones': smartphones,
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