from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
#from .forms import CreateUserForm, NoticeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
#import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group  # to assign group to new user while creation
from datetime import datetime
from django.contrib import messages

from .models import Product
from .forms import ProdutForm
from .forms import CustomerdetForm
from .forms import sellerForm
from .forms import ShipForm
from .forms import TransacForm

def index(request):  

    pr=Product.objects.filter(id=1)
    print(pr)
    context={
        'product':pr
    }
   
    return render(request,'index.html', context)



def add_product(request): 
    if request.POST:
        form=ProdutForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            # messages.success(request, "Data saved")
            instance.save()
            return redirect('product-home')
        else:
            # messages.success(request, "Data Not saved, Please check input")
            form=ProdutForm()
            return render(request,'product_entry_form.html', {'form':form})
    else:
        form=ProdutForm()
        return render(request,'product_entry_form.html', {'form':form})
def customerinfo(request): 
    if request.POST:
        form=CustomerdetForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            # messages.success(request, "Data saved")
            instance.save()
            return redirect('product-home')
        else:
            # messages.success(request, "Data Not saved, Please check input")
            form=CustomerdetForm()
            return render(request,'product_entry_form.html', {'form':form})
    else:
        form=CustomerdetForm()
        return render(request,'product_entry_form.html', {'form':form})

def sellerinfo(request): 
    if request.POST:
        form=sellerForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            # messages.success(request, "Data saved")
            instance.save()
            return redirect('product-home')
        else:
            # messages.success(request, "Data Not saved, Please check input")
            form=sellerForm()
            return render(request,'product_entry_form.html', {'form':form})
    else:
        form=sellerForm()
        return render(request,'product_entry_form.html', {'form':form})
    
def checkout(request): 
    if request.POST:
        form=ShipForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            # messages.success(request, "Data saved")
            instance.save()
            return redirect('product-home')
        else:
            # messages.success(request, "Data Not saved, Please check input")
            form=ShipForm()
            return render(request,'product_entry_form.html', {'form':form})
    else:
        form=ShipForm()
    if request.POST:
        form=TransacForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            # messages.success(request, "Data saved")
            instance.save()
            return redirect('product-home')
        else:
            # messages.success(request, "Data Not saved, Please check input")
            form=TransacForm()
            return render(request,'product_entry_form.html', {'form':form})
    else:
        form=TransacForm()
        return render(request,'product_entry_form.html', {'form':form})