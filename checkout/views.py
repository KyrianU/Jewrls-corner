from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NpHO7J42UoZUbQxGvfvHtF50G99TGvh0Zy6uc6nVhhmhRclRxjbY0nY1BQXm5r72K1U1jj1n2WHpXf6XMZH9PKu00MDYqgLHD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
