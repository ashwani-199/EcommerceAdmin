from django import forms
from apps.users.models import User

class UserAddForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Username'}),
        error_messages={
            'required': "The username field is required."
        }
    )
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'First Name'}),
        error_messages={
            'required': "The First name field is required."
        }
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Last Name'}),
        error_messages={
            'required': "The Last name field is required."
        }
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Email'}),
        error_messages={
            'required': "The email field is required."
        }
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control",
                   'placeholder': 'Password'}),
        error_messages={
            'required': "The password field is required."
        }
    )
    confirm_password = forms.CharField(
        required=True,
        label='Confire Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control",
                   'placeholder': 'Confire Password'}),
        error_messages={
            'required': "The confire password field is required."
        }
    )
    mobile_number = forms.CharField(
        required=True,
        label='Mobile Number',
        widget=forms.NumberInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Mobile Number'}),
        error_messages={
            'required': "The mobile number field is required."
        }
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'mobile_number']

class UserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Username'}),
        error_messages={
            'required': "The username field is required."
        }
    )
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'First Name'}),
        error_messages={
            'required': "The First name field is required."
        }
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Last Name'}),
        error_messages={
            'required': "The Last name field is required."
        }
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Email'}),
        error_messages={
            'required': "The email field is required."
        }
    )
    mobile_number = forms.CharField(
        required=True,
        label='Mobile Number',
        widget=forms.NumberInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Mobile Number'}),
        error_messages={
            'required': "The mobile number field is required."
        }
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number']