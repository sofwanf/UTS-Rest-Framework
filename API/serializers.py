from rest_framework import serializers
from .models import Product, Transaction, Customer

class ProductSerializer(serializers.ModelSerializer):
    Transaction = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", " stock"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "name", "product", "quantity", "transaction_date", "transaction_type"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "email", "address"]
    
