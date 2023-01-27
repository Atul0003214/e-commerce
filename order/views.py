from django.shortcuts import render, HttpResponseRedirect
from cart.models import Cart
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from customer.models import AddressModel

@login_required
def insert_order(request):
    # items = Cart.objects.filter(cart_user_id=request.user,order_completed=False) 
    # order_total = sum([item.net_price for item in items])
    # order,created = OrderModel.objects.get_or_create(customer= request.user, total=order_total,completed=False)
    # order_number = [order.id for order in OrderModel.objects.filter(id=order.id)]
    # # items.update(order_number=order_number[0],order_completed=True)
    # items.update(order_number=order_number[0])
    return HttpResponseRedirect('/order/')
    
@login_required
def order_details(request):
    # order = OrderModel.objects.filter(customer=request.user,completed=False)
    # context = {'order_items': order }
    items = Cart.objects.filter(cart_user_id=request.user,order_completed=False) 
    order_total = sum([item.net_price for item in items])
    delivery_total = sum([item.cart_prod_deli_chrg for item in items])
    net_total = order_total + delivery_total
    addr = AddressModel.objects.filter(customer=request.user.customermodel)
    print(addr)
    context = {'order_items':items,'total': order_total,'address':addr,'delivery_total':delivery_total,"net_total":net_total}
    return render(request,'order/order.html',context)

@login_required
def order_successfull(request):
    
    items = Cart.objects.filter(cart_user_id=request.user,order_completed=False) 
    order_total = sum([item.net_price for item in items])
    order,created = OrderModel.objects.get_or_create(customer= request.user, total=order_total,completed=True)
    order_number = [order.id for order in OrderModel.objects.filter(id=order.id)]
    items.update(order_number=order_number[0],order_completed=True)
    return render(request,'order/ord_complete.html')
