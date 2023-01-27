from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index-page"),
    path('productline/<line_id>',views.index,name="product_line_view"),
    path('<int:pk>',views.Product_Details_Views.as_view(),name='Product_details'),
    path('search/',views.searchView,name="Search"),
]