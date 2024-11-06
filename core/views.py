from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.core.cache import cache
from django.core.mail import send_mail

from .models import Smartphone, Brand, Category, ProductTag

class SmartphonesListView(ListView):
    model = Smartphone
    template_name = 'shop.html'
    context_object_name = 'smartphones'
    paginate_by = 9

    def get_queryset(self):

        category_slug = self.kwargs.get('category_slug')
        brand_slug = self.kwargs.get('brand_slug')
        search_query = self.request.GET.get('q')
        price_query = self.request.GET.get('rangeInput')
        tag_query = self.request.GET.get('tag-name')
        sort_by = self.request.GET.get('sort_by', '-created_at')

        cache_key = f"smartphones_queryset_{category_slug}_{brand_slug}_{search_query}_{price_query}_{tag_query}_{sort_by}"
        smartphones = cache.get(cache_key)

        if not smartphones:
            smartphones = Smartphone.objects.all()

            if category_slug:
                category = get_object_or_404(Category, slug=category_slug)
                all_categories = category.get_descendants(include_self=True)
                smartphones = smartphones.filter(category__in=all_categories)

            if brand_slug:
                brand = get_object_or_404(Brand, slug=brand_slug)
                smartphones = smartphones.filter(brand=brand)

            if search_query:
                smartphones = smartphones.filter(name__icontains=search_query)

            if price_query:
                smartphones = smartphones.filter(price__lte=price_query)

            if tag_query:
                smartphones = smartphones.filter(tags__name=tag_query)

            smartphones = smartphones.order_by(sort_by)
            smartphones = smartphones.prefetch_related('category').select_related('brand').prefetch_related('tags')

            cache.set(cache_key, smartphones, timeout=60 * 10)

        return smartphones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Categories
        categories = Category.objects.filter(parent=None)
        for category in categories:
            all_categories = category.get_descendants(include_self=True)
            category.model_count = Smartphone.objects.filter(category__in=all_categories).count()
        context['categories'] = categories
        context['brands'] = get_brands_with_products_count()
        context['total'] = self.get_queryset().count()
        context['tags'] = ProductTag.objects.all()

        # Querystring for pagination
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            del query_params['page']
        context['querystring'] = query_params.urlencode()

        # Search query
        context['search_query'] = self.request.GET.get('q', '')

        return context

class PhoneDetailView(DetailView):
    model = Smartphone
    template_name = 'phone-detail.html'
    context_object_name = 'smartphone'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Smartphone.objects.select_related('brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.object.brand
        context['smartphones'] = Smartphone.objects.filter(brand=brand).select_related('brand')
        context['brands'] = get_brands_with_products_count()
        return context

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def contact(request):
    if request.method == "POST":
        sender_name = request.POST['sender_name']
        sender_email = request.POST['sender_email']
        message = request.POST['message']

        send_mail(sender_name, message, sender_email, ["tumana991@gmail.com"])

        return render(request, 'contact.html', {"sender_name": sender_name})

    return render(request, 'contact.html')

# This view is to check error 500 manually
def check500():
    pass

def get_brands_with_products_count():

    brands = Brand.objects.all()

    for brand in brands:
        model = Smartphone.objects.filter(brand=brand)
        model_count = model.count()
        brand.model_count = model_count

    return brands