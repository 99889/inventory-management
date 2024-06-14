from django.urls import path
from . import views

urlpatterns = [
    
    path('products/', views.product_list, name='product_list'),  # List all products
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Detail of a specific product
    path('products/create/', views.create_product, name='create_product'),  # Create a new product
    path('products/update/<int:pk>/', views.update_product, name='update_product'),  # Update a product
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),  # Delete a product

    path('orders/', views.order_list, name='order_list'),  
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),  
    path('orders/create/', views.create_order, name='create_order'),  
    path('orders/update/<int:pk>/', views.update_order, name='update_order'),  
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),  



    path('stock/transfers/', views.stock_transfer_list, name='stock_transfer_list'),  
    path('stock/transfers/<int:pk>/', views.stock_transfer_detail, name='stock_transfer_detail'),  
    path('stock/transfer/', views.stock_transfer, name='stock_transfer'),  
    path('stock/transfer/update/<int:pk>/', views.update_stock_transfer, name='update_stock_transfer'),  
    path('stock/transfer/delete/<int:pk>/', views.delete_stock_transfer, name='delete_stock_transfer'),  

]
