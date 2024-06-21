
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
from products.models import User,Category,Product,FoodItem,Order,OrderItem,Transaction,Delivery,Reward,UserReward,Coin,Competition


def index(request):  

    ur=User.objects.filter()
    print(ur)
    context={
        'User':ur
    }
    ct=Category.objects.filter()
    print(ct)
    context={
        'Category':ct
    }
    pr=Product.objects.filter()
    print(pr)
    context={
        'Product':pr
    }
    Fi=FoodItem.objects.filter()
    print(Fi)
    context={
        'FoodItem':Fi
    }
    ord=Order.objects.filter()
    print(ord)
    context={
        'Order':ord
    }
    oi=OrderItem.objects.filter()
    print(oi)
    context={
        'OrderItem':oi
    }
    tn=Transaction.objects.filter()
    print(tn)
    context={
        'Transaction':tn
    }
    delv=Delivery.objects.filter()
    print(delv)
    context={
        'Delivery':delv
    }

    rew=Reward.objects.filter()
    print(rew)
    context={
        'Reward':rew
    }
    urew=UserReward.objects.filter()
    print(urew)
    context={
        'UserReward':urew   
    }
    cn=Coin.objects.filter()
    print(cn)
    context={
        'Coin':cn
    }
    comp=Competition.objects.filter()
    print(comp)
    context={
        'Competition':comp
    }

   
    return render(request,'index.html', context)