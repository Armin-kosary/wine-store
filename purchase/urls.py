from django.urls import path
from . import views
urlpatterns = [
    path('complete-purchase', views.purchase, name='purchase')
]
