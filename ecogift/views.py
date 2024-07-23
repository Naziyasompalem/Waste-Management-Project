
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

def paymentSuccessPage(request):
    return render(request,"successPage.html")


def My_Orders(request):
    # Retrieve orders for the current user
    orders = Order.objects.filter(Customer=request.user)
    
    # Retrieve order items for the retrieved orders
    order_items = OrderItem.objects.filter(Order__in=orders)
    
    return render(request, 'My_Orders.html', {'orders': orders, 'order_items': order_items})
def customerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = Customer.objects.filter(username=username, password_main=password).first()
        if user is not None:
            login(request, user)
            if user.is_seller:
                print("Seller Login successful")
                return redirect('seller-main')
            print("Customer Login successful")
            return redirect('index')
        else:
            # Add more specific debugging information
            print("Authentication failed. Checking user existence and password manually.")
            try:
                user = Customer.objects.get(username=username)
                print(f"User found: {user}")
                if user.check_password(password):
                    print("Password is correct")
                    # If it reaches here, the problem is with `authenticate` or other configurations.
                else:
                    print("Incorrect password")
            except Customer.DoesNotExist:
                print("User does not exist")
            
            messages.error(request, 'Invalid username or password')

    print("Login Failed")
    return render(request, 'LOGINPG.html')

@login_required
def customerLogout(request):
    logout(request)
    return redirect('loginCus')#home page

def fcompPage(request):
    sellers = Seller.objects.all().order_by('-sellerpoints')[:5]
    current_seller = Seller.objects.get(Customer=request.user)
    return render(request,'comp1.html',{'sellers':sellers, 'current_seller':current_seller} )

@login_required
def myaccountPage(request):
    user = request.user
    return render(request,'my_account.html',{'user': user})

def shop_detail(request,product_id):
    return render(request,'shop-detail.html')

def get_sellers_from_order(order_instance):
    # Get all OrderItem instances related to the given Order
    order_items = order_instance.orders.all()

    # Get all Products from the OrderItems
    products = Product.objects.filter(orderitem__in=order_items)

    # Get all Sellers from the Products
    sellers = Seller.objects.filter(product__in=products).distinct()

    return sellers

def sellerMain(request):
    seller = Seller.objects.get(Customer=request.user)
    products = Product.objects.filter(Seller=seller)

    # Get the latest order for the customer
    order = Order.objects.filter(Customer=request.user).last()

    # Get delivered orders for products of the current seller
    delivered_orders = Order.objects.filter(
        orders__Product__Seller=seller,
        Status='Delivered'
    ).distinct()
    active_orders = Order.objects.filter(
        orders__Product__Seller=seller,
        Status='Pending'
    ).distinct()
    income = 0
    for order in delivered_orders:
        for order_item in order.orders.all():
            income += float(order_item.Product.Price)
    incom = "%.2f"%income
    context = {
        'products': products,
        'active_orders': active_orders,
        "delivered_orders": delivered_orders,
        "income": f"{incom}"
    }
    print(delivered_orders)
    return render(request, "seller.html", context)
def Donatepg(request):
    return render(request,"Donatepage.html")
def Pricelist(request):
    return render(request,"pricelist.html")
# def Generators(request):
#     return render(request,"selldetpg.html")
def Notification(request):
    return render(request,"Notifications.html")