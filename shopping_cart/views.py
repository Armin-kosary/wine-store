from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product
from django.http import HttpResponseRedirect
# Create your views here.

# def shopping_cart_add_item(request, item):
#     print(item)
#     if request.method == 'POST':
#         product_id = {'id' : item}
#         request.session["shopping_cart"].append(product_id)
#         request.session.modified = True


def shopping_cart(request):
    if request.method == "POST":
        request.session["shopping_cart"].remove(request.POST["remove-product"])
        request.session.modified = True
        return HttpResponseRedirect(request.path_info)
    
    shopping_cart_products = []
    total_price = 0
    for item in request.session["shopping_cart"]:
        product = Product.objects.get(pk = item)
        shopping_cart_products.append(product)
        total_price += product.price

    print(shopping_cart_products)
    context = {
        'shopping_cart' : shopping_cart_products,
        'total_price' : total_price
    }
    return render(request, 'shopping_cart/shopping_cart.html', context)