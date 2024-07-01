from django import forms
from .models import Product, Category


class ProdutForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"


    