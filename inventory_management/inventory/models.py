from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_SOURCE_CHOICES = [
        ('WEBSITE', 'Website'),
        ('AMAZON', 'Amazon'),
        ('FLIPKART', 'Flipkart'),
    ]
    order_id = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=10, choices=ORDER_SOURCE_CHOICES)

    def __str__(self):
        return self.order_id

class StockTransfer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} from {self.from_location} to {self.to_location}"
