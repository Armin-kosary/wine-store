from django.urls import path
from . import views
urlpatterns = [
    path('shopping-cart', views.shopping_cart, name='shopping-cart'),
    # path('shopping-cart/<item>', views.shopping_cart_add_item, name='shopping-cart-add-item')
]
