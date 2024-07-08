from django.db import models
from django.core.validators import FileExtensionValidator
import os


class Customer(models.Model):
  Name = models.CharField(max_length=255)
  Email = models.EmailField(unique=True)
  Password = models.CharField(max_length=128)
  Address = models.CharField(max_length=255, blank=True)
  Phone = models.CharField(max_length=20, blank=True) 


class Category(models.Model):
  Name = models.CharField(max_length=255)
  def __str__(self):
    return self.Name


class Product(models.Model):
  Name = models.CharField(max_length=255)
  Description = models.TextField(blank=True)
  Price = models.CharField(max_length=10)
  Category = models.ForeignKey(Category, on_delete=models.CASCADE)
  Image = models.ImageField(upload_to='products/', blank=True)


class FoodItem(Product):
  Cuisine = models.CharField(max_length=255, blank=True)
  class Meta:
      managed = True

class Order(models.Model):
  OrderDate = models.DateTimeField(auto_now_add=True)
  STATUS_CHOICES = (
      ('Pending', 'Pending'),
      ('Processing', 'Processing'),
      ('Delivered', 'Delivered'),
      ('Cancelled', 'Cancelled'),
  )
  Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
  class Meta:
      managed = True
class OrderItem(models.Model):
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)
  Quantity = models.PositiveIntegerField()
  Price = models.DecimalField(max_digits=10, decimal_places=2)
  class Meta:
      managed = True
class Transaction(models.Model):
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  PAYMENT_METHOD_CHOICES = (
      ('Credit Card', 'Credit Card'),
      ('Cash on Delivery', 'Cash on Delivery'),
  )
  PaymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
  Amount = models.DecimalField(max_digits=10, decimal_places=2)
  class Meta:
      managed = True
class Delivery(models.Model):
  Order = models.ForeignKey(Order, on_delete=models.CASCADE)
  DeliveryPerson = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  STATUS_CHOICES = (
      ('Pending', 'Pending'),
      ('On the way', 'On the way'),
      ('Delivered', 'Delivered'),
  )
  DeliveryStatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
  DeliveryFee = models.DecimalField(max_digits=10, decimal_places=2)
  class Meta:
      managed = True
class Reward(models.Model):
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  PointsRequired = models.PositiveIntegerField()
  class Meta:
      managed = True
class UserReward(models.Model):
  Cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
  Reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
  EarnedDate = models.DateTimeField(blank=True, null=True)
  class Meta:
      managed = True


class Coin(models.Model):
  Cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
  Amount = models.PositiveIntegerField()
  class Meta:
      managed = True

class Competition(models.Model):
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  StartDate = models.DateTimeField()


class Seller(models.Model):
  """
  This model represents a seller on the e-commerce website.
  """
  ShopName = models.CharField(max_length=255)
  Email = models.EmailField(unique=True)
  # Assuming password is handled separately (e.g., hashed and stored securely)
  # Password = models.CharField(max_length=128)

  # Contact Information
  Phone = models.CharField(max_length=20, blank=True)  # Phone number with country code

  # Business Information
  CompanyAddress = models.CharField(max_length=255, blank=True)
  TaxIdentificationNumber = models.CharField(max_length=50, blank=True)  # May vary based on location

  # Pickup Address (optional for in-store pickup)
  PickupAddress = models.CharField(max_length=255, blank=True)

  # Bank Details (**sensitive, store securely!**)
  BankAccountName = models.CharField(max_length=255, blank=True)
  BankName = models.CharField(max_length=255, blank=True)
  AccountNumber = models.CharField(max_length=50, blank=True)
  # **Never store raw credit card details!**

  # Additional details (optional)
  Description = models.TextField(blank=True)  # Seller's shop description
  Website = models.URLField(blank=True)  # Seller's website URL (if applicable)


class ShippingInformation(models.Model):
  """
  This model represents shipping information for an order.
  """
  # Consider linking this model to your Order model (if applicable)
  # Order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Example foreign key

  # Customer Information (might be linked to Customer model)
  FullName = models.CharField(max_length=255)
  Email = models.EmailField(blank=True)  # Optional for guest checkout
  Phone = models.CharField(max_length=20, blank=True)  # Phone number with country code

  # Shipping Address
  AddressLine1 = models.CharField(max_length=255)
  AddressLine2 = models.CharField(max_length=255, blank=True)  # Optional for additional address details
  City = models.CharField(max_length=100)
  State = models.CharField(max_length=100)  # Adjust field length based on your location
  PostalCode = models.CharField(max_length=20)
  Country = models.CharField(max_length=100)
  

  # Additional Information (optional)
  ShippingInstructions = models.TextField(blank=True)  # Special delivery instructions
  ShippingMethod = models.CharField(max_length=100, blank=True)  # Chosen shipping method (e.g., standard, express)


class Meta:
  managed = True
  def __str__(self):
    return str(self.Name)
