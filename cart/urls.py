from django.urls import path,include
from . import views


urlpatterns = [
    path('cart/<int:p_id>', views.createCartItem,name='create_cart'),
    path('cart/<int:p_id>/<order>', views.createCartItem,name='create_cart_order'),
    path('cart/', views.cartItem,name='view_items'),
    path('updateQuantity/', views.update_quantity,name='update_Quantity'),
    
    
]