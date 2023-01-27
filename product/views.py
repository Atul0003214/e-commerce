from django.shortcuts import render
from .models import Product, Product_category, Product_line
from django.views.generic.detail import DetailView


def index(request,line_id=""):
    productCat_dict = {}
    prod_cat = Product_category.objects.all()
    for m in prod_cat:
        prod_line = Product_line.objects.filter(Product_category_F = m.id)
        productline_dict = {}
        for line in prod_line:
            prod_list = Product.objects.filter(product_line_F = line.id)
            productline_dict[line.product_line] = prod_list
            productCat_dict[m.product_cat] = productline_dict
            
    if line_id != "":
        line = Product_line.objects.get(product_line=line_id)
        product_list = Product.objects.filter(product_line_F=line.id)
    else:
        product_list = Product.objects.all()
    
    context = {'productCat_dict': productCat_dict,'product_list':product_list}
    return render(request,"product/home.html",context)


class Product_Details_Views(DetailView):
    model = Product
    context_object_name = 'prod_detail'
    productCat_dict = {}
    prod_cat = Product_category.objects.all()
    for m in prod_cat:
        prod_line = Product_line.objects.filter(Product_category_F = m.id)
        productline_dict = {}
        for line in prod_line:
            prod_list = Product.objects.filter(product_line_F = line.id)
            productline_dict[line.product_line] = prod_list
            productCat_dict[m.product_cat] = productline_dict
    extra_context = {'productCat_dict':productCat_dict}


def searchView(request):
    if request.method == "POST":
        param = request.POST['searchpart']
        productCat_dict = {}
        prod_cat = Product_category.objects.all()
        for m in prod_cat:
            prod_line = Product_line.objects.filter(Product_category_F = m.id)
            productline_dict = {}
            for line in prod_line:
                prod_list = Product.objects.filter(product_line_F = line.id)
                productline_dict[line.product_line] = prod_list
                productCat_dict[m.product_cat] = productline_dict 
        if param != "":
            product_list = Product.objects.filter(product_name__contains=param)
        else:
            product_list = Product.objects.all()
        context = {'productCat_dict': productCat_dict,'product_list':product_list}
        return render(request,"product/home.html",context)
        

