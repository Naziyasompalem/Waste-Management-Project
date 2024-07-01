from django import forms
from .models import Product, Category

class ProdutForm(forms.ModelForm):
    class Meta:
        model=Product

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
    