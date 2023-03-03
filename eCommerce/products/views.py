from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProductSerializer, OrderSerializer
from .models import Product, Order
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class Product(ReadOnlyModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_fields = [
        'quantity'
    ]
    search_fields = [
        'name',
        'description'
    ]
    queryset = Product.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = ProductSerializer


class Order(ModelViewSet):
    http_method_names = [
        'get',
        'post'
    ]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
