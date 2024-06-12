from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Order, StockTransfer

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from .models import Product, Order, StockTransfer
from django.views.decorators.csrf import csrf_exempt
import json

def product_list(request):
    products = Product.objects.all()
    return JsonResponse({"products": list(products.values())})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({"product": {
        "name": product.name,
        "sku": product.sku,
        "description": product.description,
        "price": product.price,
        "quantity": product.quantity,
    }})

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data['product_id']
            quantity = data['quantity']
            source = data['source']
            
            # Validate order source
            if source not in dict(Order.ORDER_SOURCE_CHOICES):
                return HttpResponseBadRequest("Invalid order source")

            product = get_object_or_404(Product, id=product_id)
            
            # Check if there's enough stock
            if product.quantity < quantity:
                return HttpResponseBadRequest("Not enough stock available")

            # Create the order
            order = Order.objects.create(
                product=product,
                quantity=quantity,
                source=source
            )

            # Update the product's stock
            product.quantity -= quantity
            product.save()

            return JsonResponse({"order_id": order.order_id}, status=201)
        
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")

    return HttpResponseBadRequest("Only POST method is allowed")

@csrf_exempt
def stock_transfer(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data['product_id']
            from_location = data['from_location']
            to_location = data['to_location']
            quantity = data['quantity']
            
            product = get_object_or_404(Product, id=product_id)

            # Check if there's enough stock at the source location
            if product.quantity < quantity:
                return HttpResponseBadRequest("Not enough stock available")

            # Create the stock transfer
            stock_transfer = StockTransfer.objects.create(
                product=product,
                from_location=from_location,
                to_location=to_location,
                quantity=quantity
            )

            # Update the product's stock
            product.quantity -= quantity
            product.save()

            return JsonResponse({"stock_transfer_id": stock_transfer.id}, status=201)
        
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")

    return HttpResponseBadRequest("Only POST method is allowed")