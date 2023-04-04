from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """A view to show all the products, including sorting and search queries"""

    products = Product.objects.all()

    context = {
        'products': products,

    }
    template = 'products/products.html'

    return render(request, template, context)
