from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Product, Transaction, Customer
from .serializers import ProductSerializer, TransactionSerializer, CustomerSerializer


@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Product_list(request, format=None):

    if request.method == 'GET':
        Product = Product.objects.all()
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Product_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Transaction_list(request, format=None):

    if request.method == 'GET':
        Transaction = Transaction.objects.all()
        serializer = TransactionSerializer(Transaction, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def Transaction_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(Transaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TransactionSerializer(Transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Customer_list(request, format=None):

    if request.method == 'GET':
        Customer = Customer.objects.all()
        serializer = CustomerSerializer(Customer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def Customer_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(Customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(Customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)