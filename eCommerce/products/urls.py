from django.urls import path, include
from .views import Product, Order
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', Product, basename='product')
router.register('order', Order, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]
