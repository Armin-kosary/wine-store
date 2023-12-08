from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CompletePurchaseForm
from .models import Order
from product.models import Product
# Create your views here.

def purchase(request):
    form = CompletePurchaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            total_price = 0
            for item in request.session["shopping_cart"]:
                product = Product.objects.get(pk = item)
                total_price += product.price

            new_order = Order(
                first_name = form.cleaned_data.get("first_name"),
                last_name = form.cleaned_data.get("last_name"),
                address = form.cleaned_data.get("address"),
                phone = form.cleaned_data.get("phone"),
                # products = request.session["shopping_cart"],
                price = total_price
            )
            new_order.save()
            for product in request.session["shopping_cart"]:
                import_product = Product.objects.get(pk = product)
                new_order.products.add(import_product)
            request.session["shopping_cart"] = []
            request.session.modified = True
            return redirect(reverse('home-page'))
    context = {
        'form' : form
    }
    return render(request, 'purchase/user-info.html', context)