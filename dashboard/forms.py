from django import forms
from food.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "created_at":forms.TextInput(attrs={'class':'form-control'})
        }

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "image":forms.TextInput(attrs={"class":"form-control"}),
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={'class':"form-control"}),
            "cost":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "created_at":forms.TextInput(attrs={"class": "form_control"})

        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
            "created_at":forms.TextInput(attrs={'class':"form-control"})
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "payment_type":forms.TextInput(attrs={"class":"form-control"}),
            "status":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "customer":forms.Select(attrs={"class":"form-control"})
        }