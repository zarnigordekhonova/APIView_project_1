from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import Category, Products
from .serializers import CategorySerializer, ProductsListSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView


# Create your views here.

class ProductsCreateView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer


class CategoryCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProductsView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer


class ListCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer


class CategoryDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

