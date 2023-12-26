from django.urls import path
from .views import product_detail_view

urlpatterns = [
    path('products/', product_detail_view)
]
