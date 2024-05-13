from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=[('Pembelian', 'Pembelian'), ('Penjualan', 'Penjualan')])

    def __str__(self):
        return self.quantity
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
                                        
