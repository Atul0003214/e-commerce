from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_details,name='cart_items'),
    path('create_order/', views.insert_order,name='create_order'),
    path('order_successfull/', views.order_successfull,name='order_successfull'),
    
]