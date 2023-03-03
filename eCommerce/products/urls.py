from django.urls import path
from .views import Product, Order

urlpatterns = [
    path('product/', Product.as_view(), name='Product'),
    path('order/<int:id>/', Order.as_view(), name='order'),
]
