from django.contrib import admin
# Register your models here.
from .models import Product ,Product_line, Product_category

@admin.register(Product_category)
class ProdCatAdmin(admin.ModelAdmin):
    list_display = ['product_cat','product_cat_slug']



@admin.register(Product_line)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ['product_line','product_line_slug','Product_category_F']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_desc','product_quantity','product_price','product_name_slug']