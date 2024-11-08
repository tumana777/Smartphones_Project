from django.core.management.base import BaseCommand
from django.db.models import Count
from core.models import Smartphone
from order.models import CartItem

class Command(BaseCommand):
    help = 'Populates database with popular products based on user carts'

    def handle(self, *args, **options):
        popular_products = (
            CartItem.objects
            .values('product')
            .annotate(count=Count('product'))
            .order_by('-count')[:3]
        )

        for product in popular_products:
            print(f"{Smartphone.objects.get(pk=product['product'])} --> in {product['count']} user's carts")

        self.stdout.write(self.style.SUCCESS('Found 3 popular products'))