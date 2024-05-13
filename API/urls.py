from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('Product/', views.Product_list),
    path('Product/<int:pk>/', views.Product_detail),
    path('Transaction/', views.Transaction_list),
    path('Transaction/<int:pk>/', views.Transaction_detail),
    path('Customer/', views.Customer_list),
    path('Customer/<int:pk>/', views.Customer_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)