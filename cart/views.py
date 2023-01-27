from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from product.models import Product
from .models import Cart
from django.urls import reverse
from customer.models import CustomerModel
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def createCartItem(request,p_id,order='addToCart'):
    prodIntance, created = Product.objects.get_or_create(id=p_id)
    cart_record = Cart(cart_product_name=prodIntance.product_name,cart_product_desc=prodIntance.product_desc,cart_prod_quantity=prodIntance.product_quantity,
    cart_product_price=prodIntance.product_price,cart_product_discount=prodIntance.product_discount,cart_prod_sell_price=prodIntance.product_sell_price
    ,cart_prod_deli_chrg=prodIntance.prod_delivery_charge,cart_user_id=request.user,product=prodIntance)
    
    # cart_record = Cart(cart_product_name=prodIntance.product_name,cart_product_desc=prodIntance.product_desc,cart_prod_quantity=prodIntance.product_quantity,
    # cart_product_price=prodIntance.product_price,cart_product_discount=prodIntance.product_discount,cart_prod_sell_price=prodIntance.product_sell_price
    # ,cart_prod_net_price=prodIntance.product_net_price,cart_prod_deli_chrg=prodIntance.prod_delivery_charge,cart_prod_total=prodIntance.product_net_price,cart_user_id=request.user,product=prodIntance)
    
    cart_record.save()

    cart_rec = Cart.objects.all()
    context = {'cart_rec':cart_rec}
    if order == "order":
        return HttpResponseRedirect(reverse('create_order') )
    else:
        return HttpResponseRedirect('/cart/')

@login_required
def cartItem(request):
    cart_rec = Cart.objects.filter(cart_user_id=request.user,order_completed=False)
    total = 0;  del_charge = 0;  net_total=0; list_total = 0; discount=0
    for i in cart_rec:
        total += i.net_price
        del_charge += i.cart_prod_deli_chrg
        list_total += i.net_list_price
    net_total = del_charge + total
    discount = list_total -total
    context = {'cart_rec':cart_rec,'total':total,'del_charge':del_charge,"net_total":net_total,'discount':discount}
    return render(request,'cart/cart.html', context)


@login_required
def update_quantity(request):
    data = json.loads(request.body)
    row_id = data['cartID']
    action = data['action']
    cart_row_quantity = Cart.objects.get(id=row_id).cart_prod_quantity
    if action == 'increase':
        cart_row_quantity += 1
    if action == 'reduce':
        cart_row_quantity-=1

    if cart_row_quantity<1:
        Cart.objects.filter(id = row_id).delete()

    Cart.objects.filter(id=row_id).update(cart_prod_quantity = cart_row_quantity)
    return JsonResponse("Working response",safe=False)