from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,

    }
    template = 'products/product_detail.html'

    return render(request, template, context)
