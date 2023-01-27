from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from .models import AddressModel
from order.models import OrderModel
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def customer_details(request):
    context = {}
    return render(request,'customer/cus_details.html',context)

@login_required
def add_address(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        inputAddress = request.POST['inputAddress']
        inputAddress2 = request.POST['inputAddress2']
        inputCity = request.POST['inputCity']
        inputState = request.POST['inputState']
        inputZip = request.POST['inputZip']
        cust = request.user.customermodel
        # orderNumber,created = OrderModel.objects.get_or_create(customer=request.user,completed=False)
        form = AddressModel(customer=cust,Address=inputAddress,Address2=inputAddress2,city=inputCity,state=inputState,zip=inputZip,fName=first_name,lName=last_name,current_address=True)
        form.save()
        
        # if orderNumber:
        
        #     form = AddressModel(customer=cust,order=orderNumber,Address=inputAddress,Address2=inputAddress2,city=inputCity,state=inputState,zip=inputZip,fName=first_name,lName=last_name)
        #     form.save()

    return HttpResponseRedirect('/order/')


def update_address(request):
    if request.method == 'POST':
        row_id = request.POST['row_identifier']
        # print(row_id)
        if row_id is not None:
            AddressModel.objects.all().update(current_address=False)
            AddressModel.objects.filter(id = row_id).update(current_address=True)

    return HttpResponseRedirect('/order/')
