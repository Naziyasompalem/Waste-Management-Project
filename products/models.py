from django.db import models
from django.core.validators import FileExtensionValidator
import os


class Customer(models.Model):
  Name = models.CharField(max_length=255)
  Email = models.EmailField(unique=True)
  Password = models.CharField(max_length=128)
  Address = models.CharField(max_length=255, blank=True)


class Category(models.Model):
  Name = models.CharField(max_length=255)


class Product(models.Model):
  Name = models.CharField(max_length=255)
  Description = models.TextField()
  Price = models.DecimalField(max_digits=10, decimal_places=2)
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

  class Meta:
      managed = True
  def __str__(self):
      return str(self.Name)