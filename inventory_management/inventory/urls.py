from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('orders/create/', views.create_order, name='create_order'),
    path('stock/transfer/', views.stock_transfer, name='stock_transfer'),
]
