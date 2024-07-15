
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

# from products.models import Product
from products.models import Customer,Category,Product,FoodItem,Order,OrderItem,Delivery,Transaction,Reward,UserReward,Coin,Competition,Seller,ShippingInformation


def index(request):  

    ur=Customer.objects.filter()
    
    pr=Product.objects.filter()
    Fi=FoodItem.objects.filter()
    ord=Order.objects.filter()
    oi=OrderItem.objects.filter()
    tn=Transaction.objects.filter()
    delv=Delivery.objects.filter()
    Sell=Seller.objects.filter()
    ship=ShippingInformation.objects.filter()

    
    #agriwaste=Product.objects.filter(Category_id__Name='Agricultural waste')


    ct=Category.objects.filter()
    cat=list(ct.values_list('Name', flat=True))
    print(cat)
    
    prd_all = [dict() for x in range(len(cat))]
    i=0
    for c in cat:
        prd=Product.objects.filter(Category_id__Name=c)
        #print(prd)
        prd_all[i]={**prd_all[i],**{prd:prd}}
        i+=1
    print(prd_all)
    context={'cat':cat,
             'prd_all':prd_all
        
    }
    return render(request, 'index.html', context)
    
    
    """return render(request,'index.html', context)
    categories = Category.objects.all()  # More efficient than filtering all categories
    products_by_category = {category.Name: Product.objects.filter(category=category) for category in categories}

    context = {
        'categories': categories,
        'products_by_category': products_by_category,
    }
    return render(request, 'index.html', context)"""
"""def index(request):
    categories = Category.objects.all()  # More efficient than filtering all categories
    products_by_category = {category.Name: Product.objects.filter(category=category) for category in categories}

    context = {
        'categories': categories,
        'products_by_category': products_by_category,
    }
    return render(request, 'index.html', context)"""


def shop(request):  

    ur=Customer.objects.filter()
    
    pr=Product.objects.filter()
    Fi=FoodItem.objects.filter()
    
    context={
        'ur':ur,
        'Fi':Fi

    }
    return render(request,'shop.html', context)

from django.contrib.auth.hashers import make_password
def customerLogin(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(Customer.objects.filter(email=email).values())
        username = Customer.objects.filter(email=email).username
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect('index')
    print("Login Failed")
    return render(request,'clogin.html')
