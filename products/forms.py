from django import forms
from .models import Product, Category,Customer,Seller,ShippingInformation,Transaction


class ProdutForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        exclude = ['Seller']

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
        exclude = ['sellerPoints']
class CustomerdetForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class sellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields="__all__"
        exclude = ['Customer']
class ShipForm(forms.ModelForm):
    class Meta:
        model=ShippingInformation
        fields="__all__"
class TransacForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class bulkdataform(forms.Form):
    file = forms.FileField()

    