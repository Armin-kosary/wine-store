from django.shortcuts import render
from product.models import Product
# Create your views here.

def home(request):
    if "shopping_cart" not in request.session:
        request.session["shopping_cart"] = []

    if request.method == 'POST':
        product_id = request.POST["product_id"]
        request.session["shopping_cart"].append(product_id)
        request.session.modified = True
        print(request.session["shopping_cart"])

    context = {
        'product' : Product.objects.all()
    }
    return render(request, 'home/home.html', context)