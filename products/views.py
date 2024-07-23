from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
#from .forms import CreateUserForm, NoticeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .models import Product, Cart, CartItem, Seller, FoodItem
import requests
#import json
from django.contrib.auth.models import Group  # to assign group to new user while creation
from datetime import datetime
from django.contrib import messages

from .models import Product,Category,Customer,ExtraItem
from .forms import ProdutForm
from .forms import CustomerdetForm
from .forms import sellerForm
from .forms import ShipForm
from .forms import TransacForm

import json

def mapbox_api_call(request):
    longitude = float(request.GET.get('longitude'))
    latitude = float(request.GET.get('latitude'))
    location = get_location(longitude, latitude)
    if not location:
        return JsonResponse({'error': 'Unable to find location'})
    print(location)
    # sellers = Seller.objects.filter(CompanyAddress=location)
    products = FoodItem.objects.filter(Seller__CompanyAddress=location)
    print(list(products))
    return JsonResponse({
        'location': location,
        'products': list(products)
    })

def get_location(longitude, latitude):
    url = f"https://api.mapbox.com/search/geocode/v6/reverse?longitude={longitude}&latitude={latitude}&proximity=ip&access_token={settings.MAPBOX_API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            location = posts['features'][0]['properties']['context']['locality']['name']
            print(location)
            return location
        else:
            return None
    except:
        return None


def index(request):
    categories = Category.objects.all()
    RecycleCat = Category.objects.get(Name = 'Recycled Products')
    recycledProducts = Product.objects.filter(Category = RecycleCat)
    products_by_category = {}

    for category in categories:
        products = Product.objects.filter(Category=category)
        products_by_category[category.Name] = products


    context = {
        'categories': categories,
        'products_by_category': products_by_category,
        'recycledProducts': recycledProducts
    }
    return render(request,'index.html', context)
from .models import Seller
@login_required
def add_product(request): 
    if request.POST:
        form=ProdutForm(request.POST,request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            seller = Seller.objects.get(Customer=request.user)
            instance.Seller = seller
            print(request.user)
            # messages.success(request, "Data saved")
            instance.save()
            products = Product.objects.filter(Seller=seller)
            points = sum(int(float(product.Price)) for product in products)
            print(points)
            Sinstance = Seller.objects.get(Customer=request.user)
            Sinstance.sellerpoints = int(points)
            Sinstance.save()
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


@login_required
def sellerinfo(request):
    if request.method == 'POST':
        form = sellerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Customer = request.user  # Assign the logged-in user
            instance.save()
            return redirect('seller-main')
        else:
            form = sellerForm()
            return render(request, 'product_entry_form.html', {'form': form})
    else:
        form = sellerForm()
        return render(request, 'product_entry_form.html', {'form': form})

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
    
"""def shopDetails(request,product_id):
    categories = Category.objects.all()
    #comment = objects.all()
    
    products_by_category = {Category.Name: Product.objects.filter(Category=category) for category in categories}
    product = get_object_or_404(Product, id=product_id)
    print(categories.values,products_by_category,product)
    return render(request, 'shop-detail.html', {'cat': categories, 'prd_all': products_by_category,'product':product})"""
@login_required
def shopDetails(request, product_id):
    categories = Category.objects.all()
    products_by_category = {category.Name: Product.objects.filter(Category=category) for category in categories}
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_seller:
        extra_items = ExtraItem.objects.filter(product=product)
        extra_items.update(read=True)
    else:
        extra_items = ExtraItem.objects.filter(product=product, customer=request.user)  # Show all unanswered queries by default for customers (assuming customer has a foreign key to ExtraItem)
    
    # Optional: Filter ExtraItems further based on customer if needed
    # (e.g., only show customer's own queries or queries addressed to them)
    # if request.user.is_authenticated:
    #     current_customer = request.user  # Assuming a ForeignKey from User to Customer
    #     filtered_extra_items = extra_items.filter(Q(customer=current_customer))  # Filter for customer-related queries or queries addressed to the seller (assuming seller has a customer field)
    #     extra_items = filtered_extra_items  # Update extra_items with filtered list
    products = Product.objects.filter(Category=product.Category)
    context = {
        'cat': categories,
        'prd_all': products_by_category,
        'product': product,
        'products': products,
        'extra_items': extra_items, # Include ExtraItems in the context
    }

    return render(request, 'shop-detail.html', context)
def contactus_request(request):
    print(request)
    if request.method == "POST":
        data = json.loads(request.body)
        # send email using SMTP
        send_wait_mail(data)
        return JsonResponse({
            "message": "Success"
        })

def contactus(request):
    return render(request, 'contact.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem

@login_required
def checkout_call(request):
    customer = request.user
    try:
        cart = Cart.objects.get(customer=customer)
    except Cart.DoesNotExist:
        # Handle the case where the cart doesn't exist
        return redirect('cart')  # Redirect to cart page or show an error

    # Create a new order
    order = Order.objects.create(Customer=customer, Status='Pending')

    # Add cart items to order items
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        OrderItem.objects.create(
            Order=order,
            Product=item.product,
            Quantity=item.quantity,
            Price=item.product.Price
        )

    # Clear the cart
    cart_items.delete()
    cart.delete()

    order_items = OrderItem.objects.filter(Order=order)
    return render(request,'My_orders.html',{'order': order, 'order_items': order_items})




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        #print("product reviced with the id : " + product_id)
        cart, created = Cart.objects.get_or_create(customer=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

            return JsonResponse({'message': 'Product added to cart'})
       
    return JsonResponse({'error': 'Invalid request'}, status=400)


def increment_product(request, cartItem_id, quantity):
    cart_item = get_object_or_404(CartItem, id=cartItem_id)
    cart_item.quantity = int(quantity)
    cart_item.save()
    return redirect('cart')


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem

# @login_required
def view_cart(request):
    try:
        cart = Cart.objects.get(customer=request.user)
        print(cart)
        
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            print(cart_items)
            # cart_items = cart.values.all()
            subtotal = sum(float(item.product.Price) * float(item.quantity) for item in cart_items)
        else:
            cart_items = []
            subtotal = 0
        
        context = {
            'cart': cart,
            'cart_items': cart_items,
            'subtotal': subtotal,
        }
        print(cart_items)
        return render(request, 'cart.html', context)
    
    except Cart.DoesNotExist:
        return render(request, 'cart.html', {'cart': None, 'cart_items': [], 'subtotal': 0})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'cart.html', {'cart': None, 'cart_items': [], 'subtotal': 0})


#Loading the reference data  warning:load only if the data is missed 
#else can cause constrain inssues in the database
'''
related_products = {
    "Non-Eatable Wastes": [
        "Egg Shells", "Fruit Peels", "Tea Bags", "Coffee Grounds", "Bones", 
        "Nut Shells", "Expired Bread", "Used Paper Towels", "Banana Peels", "Coconut Shells"
    ],
    "Eatable Leftovers": [
        "Leftover Pizza", "Leftover Pasta", "Leftover Rice", "Leftover Salad", "Leftover Soup", 
        "Leftover Sandwiches", "Leftover Stir Fry", "Leftover Baked Goods", "Leftover Meat", "Leftover Vegetables"
    ],
    "Plastic Waste": [
        "Plastic Bottle", "Plastic Bag", "Plastic Straw", "Plastic Wrap", "Plastic Container", 
        "Plastic Cutlery", "Plastic Packaging", "Plastic Cups", "Plastic Toys", "Plastic Lids"
    ],
    "Agriculture Waste": [
        "Corn Husks", "Straw", "Hay", "Crop Residue", "Weeds", 
        "Plant Trimmings", "Grass Clippings", "Manure", "Sawdust", "Fruit Scraps"
    ]
}

def generate_related_products(related_products):
    products = []
    for category, items in related_products.items():
        for item in items:
            products.append({
                "Name": item,
                "Description": fake.sentence(),
                "Price": str(round(random.uniform(1.0, 100.0), 2)),
                "Category": category,
                "Image": fake.image_url()
            })
    return products

related_specific_products = generate_related_products(related_products)

df_related_specific_products = pd.DataFrame(related_specific_products)

# Create new Excel writer
with pd.ExcelWriter('/mnt/data/related_specific_models_data.xlsx') as writer:
    df_specific_categories.to_excel(writer, sheet_name='Category', index=False)
    df_related_specific_products.to_excel(writer, sheet_name='Product', index=False)

'/mnt/data/related_specific_models_data.xlsx'
'''
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from products.models import Customer

def signup(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        role = request.POST.get('role')
        is_seller = True if (role == 'seller') else False
        print(username, password, email, first_name)
        # Check for existing username or email
        if Customer.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'signup.html')
        print("Completed")
        try:
            # Create the user using create_user method
            user = Customer.objects.create_user(username=username, email=email, password_main=password, first_name=first_name,is_seller=is_seller)
            user.save()
            login(request, user)
            if user.is_seller:
                messages.success(request, 'Signup successful. You can now log in.')
                return redirect('seller-det')
            return redirect('loginCus')
        except Exception as e:
            print(e)
            messages.error(request, f'Error: {e}')
            return render(request, 'signup.html')
    return render(request, 'signup.html')


def My_Orders(request):

    return render(request, 'My_orders.html')

import smtplib
from email.mime.text import MIMEText

def send_wait_mail(data):
    # Set up email server
    sender_email = "Ecogiftbusiness@outlook.com"
    sender_password = "Ecogift@2022"
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    recipient_email = data['email']

    # Create message
    subject = "EcoGift - For environment"
    body = f"Greetings {data['name']},\n\nWe have received your response. Our support team will reach you within 45 to 60 minutes. Thank you for reaching out to us.\n\nReplying to: {data['message']}"
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email
    # Connect to the server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # Log in to the email account
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Response sent successfully.")


# def checkout_call(request):
#     return render(request,"paymentPage.html")

def paymentSuccessPage(request):
    return render(request,"successPage.html")

"""from .forms import bulkdataform
import pandas as pd
import os
from django.core.files.temp import NamedTemporaryFile
from django.core.files.base import ContentFile

def bulkdata_call(request):
    if request.method == 'POST':
        form = bulkdataform(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for index, row in df.iterrows():
                image_url = row['Image (Search Term)']
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(requests.get(image_url).content)
                img_temp.flush()

                product = Product(
                    Category=Category.objects.get_or_create(Name=row['Category'])[0],
                    Name=row['Product Name'],
                    Description=row['Description'],
                    Price=row['Price (INR)'],
                )
                product.Image.save(f"{row['Product Name']}.jpg", ContentFile(img_temp.read()), save=True)
                img_temp.close()
                print("Saved")
            messages.success(request, 'Products uploaded successfully!')
            return redirect('bulkdata')
    else:
        form = bulkdataform()
    return render(request, 'bulk.html', {'form': form})"""

def DiscardItem(request,CartItem_id):
    item = CartItem.objects.get(id=CartItem_id)
    item.delete()
    return redirect('cart')

from django.db.models import Q
def search(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(Name__icontains=query)
        print(products)
        return render(request, 'search.html', {'products': products})
    return redirect('index')

# from django.core.url.resolvers import reverse
from django.http import HttpResponseRedirect
def add_query(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        customer = request.user
        product = Product.objects.get(id=int(request.POST.get('product_id')))
        print(query, customer, product)
        extra_item = ExtraItem(product=product, query=query, customer=customer)
        extra_item.save()
        return HttpResponseRedirect(reverse('shop-details', kwargs={'product_id': product.id}))

def accept_query(request, Query_id):
    query = ExtraItem.objects.get(id=Query_id)
    query.flag = "Accepted"
    query.save()
    return HttpResponseRedirect(reverse('shop-details', kwargs={'product_id': query.product.id}))


def decline_query(request, Query_id):
    query = ExtraItem.objects.get(id=Query_id)
    query.flag = "Rejected"
    query.save()
    return HttpResponseRedirect(reverse('shop-details', kwargs={'product_id': query.product.id}))

def notifications_view(request):
    extra_items = ExtraItem.objects.all().order_by('time_posted')
    notifications = {}
    for item in extra_items:
        if str(item.time_posted.date()) in notifications:
            notifications[str(item.time_posted.date())].append(item)
        else:
            notifications[str(item.time_posted.date())] = [item]
    print(notifications)
    return render(request, "notifications.html", context={
        "notifications": notifications,
    })