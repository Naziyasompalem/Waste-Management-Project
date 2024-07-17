from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
#from .forms import CreateUserForm, NoticeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .models import Product, Cart, CartItem
import requests
#import json
from django.contrib.auth.models import Group  # to assign group to new user while creation
from datetime import datetime
from django.contrib import messages

from .models import Product,Category,Customer
from .forms import ProdutForm
from .forms import CustomerdetForm
from .forms import sellerForm
from .forms import ShipForm
from .forms import TransacForm


def mapbox_api_call(request):
    longitude = float(request.GET.get('longitude'))
    latitude = float(request.GET.get('latitude'))
    location = get_location(longitude, latitude)
    if not location:
        return JsonResponse({'error': 'Unable to find location'})
    print(location)
    sellers = Seller.objects.filter(CompanyAddress=location)
    # need to add query to get food items amd send as response
    return JsonResponse({'location': location})

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
    products_by_category = {}

    for category in categories:
        products = Product.objects.filter(Category=category)
        products_by_category[category.Name] = products


    context = {
        'categories': categories,
        'products_by_category': products_by_category
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
    
def shopDetails(request):
    categories = Category.objects.all()
    products_by_category = {Category.Name: Product.objects.filter(Category=category) for category in categories}
    print(categories.values,products_by_category)
    return render(request, 'shop-detail.html', {'cat': categories, 'prd_all': products_by_category})

def contactus(request):
    return render(request, 'contact.html')



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




from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem

@login_required
def view_cart(request):
    try:
        cart = Cart.objects.filter(customer=request.user).first()
        
        if cart:
            cart_items = cart.items.all()
            subtotal = sum(item.product.Price * item.quantity for item in cart_items)
        else:
            cart_items = []
            subtotal = 0
        
        context = {
            'cart': cart,
            'cart_items': cart_items,
            'subtotal': subtotal,
        }
        
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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')

        # Check for existing username or email
        if Customer.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'signup.html')

        try:
            # Create the user using create_user method
            user = Customer.objects.create_user(username=username, email=email, password_main=password, first_name=first_name)
            user.save()
            messages.success(request, 'Signup successful. You can now log in.')
            return redirect('loginCus')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return render(request, 'signup.html')

    return render(request, 'signup.html')

