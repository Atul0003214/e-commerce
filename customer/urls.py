from django.urls import path
from . import views

urlpatterns = [
    # path('',views.customer_details,name="customer_details"),
    path('add-address/',views.add_address,name="add_address"),
    path('update_address/',views.update_address,name="update_address"),
]