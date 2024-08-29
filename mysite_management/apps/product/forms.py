from django import forms
from apps.product.models import Product,ProductCategory

class ProductForm(forms.ModelForm):
    
    # vendor = forms.ModelChoiceField(
    #     queryset=VendorProfile.objects.all(),
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple(
    #         attrs={'class': "form-control",}
    #     )
    # )
    
    categories = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': "form-control",}
        )
    )
    
    name = forms.CharField(
        required=True, 
        label='Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Name'}),
        error_messages={
            'required': "The name field is required."
        }
    )
    description = forms.CharField(
        required=True, 
        label='Description',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Description'}),
        error_messages={
            'required': "The description field is required."
        }
    )

    price = forms.CharField(
        required=True, 
        label='Price',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Price'}),
        error_messages={
            'required': "The price field is required."
        }
    )
    quantity = forms.CharField(
        required=True, 
        label='Quantity',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Quantity'}),
        error_messages={
            'required': "The quantity field is required."
        }
    )

    
    class Meta:
        model = Product
        fields = ['categories', 'name', 'description', 'price', 'quantity']