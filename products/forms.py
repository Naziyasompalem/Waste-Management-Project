from django import forms
from .models import Product, Category,Customer,Seller


class ProdutForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
class CustomerdetForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class sellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields="__all__"

    