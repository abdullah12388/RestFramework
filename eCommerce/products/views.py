from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderSerializer
from .models import Products, Orders
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


class Product(APIView, LimitOffsetPagination):
    def get(self, request, format=None):
        print(request.data.get('search'))
        products = Products.objects.all()
        results = self.paginate_queryset(products, request, view=self)
        ser = ProductSerializer(results, many=True).data
        return self.get_paginated_response(ser)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(User.objects.get(id=serializer.validated_data['user'].id))
            order_model = Orders()
            order_model.product_name = serializer.validated_data['name']
            order_model.product_quantity = serializer.validated_data['quantity']
            order_model.status = 'under-progress'
            order_model.user = User.objects.get(id=serializer.validated_data['user'].id)
            print(order_model.product_name)
            print(order_model.product_quantity)
            print(order_model.status)
            print(order_model.user)
            order_model.save()
            serializer.save()
            return Response(serializer.data)


class Order(APIView):
    def get(self, request, id, format=None):
        user_obj = User.objects.get(id=id)
        order_query = Orders.objects.filter(user=user_obj)
        order_ser = OrderSerializer(order_query, many=True).data
        return Response(order_ser)

# class Order(CreateAPIView):
#     serializer_class = OrderSerializer
#     queryset = Orders.objects.all()
