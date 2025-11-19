from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"