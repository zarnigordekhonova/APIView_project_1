from django.urls import path
from .views import ProductsCreateView, CategoryCreateView, ListProductsView, ListCategoryView, DetailsUpdateDeleteView, CategoryDeleteUpdateView

urlpatterns = [
    path('create/', ProductsCreateView.as_view(), name='create'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('products_list/', ListProductsView.as_view(), name='products_list'),
    path('category_list/', ListCategoryView.as_view(), name='category_list'),
    path('detail_update_delete/<int:pk>', DetailsUpdateDeleteView.as_view(), name='detail_update_delete'),
    path('category_update_delete/<int:pk>', CategoryDeleteUpdateView.as_view(), name='category_update_delete')
]