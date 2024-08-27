from django import forms
from apps.users.models import User

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
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']



class LoginForm(forms.Form):
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

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'class': "form-control"}),
        error_messages={
            'required': "The first name field is required"
        }
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': "form-control"}),
        error_messages={
            'required': "The last name field is required"
        }
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(attrs={'class': "form-control"}),
        error_messages={
            'required': "The email field is required",
            'invalid': "The email is not valid"
        }
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# Forgot Password Form
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   'placeholder': "Email"}),
        error_messages={
            'required': "The email_field_is_required",
            'invalid': "The email_is_not_valid",
            'exists': "The email_is_not_exists"
        }
    )

class PasswordRestForm(forms.Form):
    new_password = forms.CharField(
        required=False,
        label='New Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control ",
                   'placeholder': "New password"}),
        error_messages={
            'required': "The new password field is required.",
            'min_value': "The confirm password should contains at least 8 digits",
        }
    )
    confirm_password = forms.CharField(
        required=False,
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control",
                   'placeholder': "Confirm password"}),
        error_messages={
            'required': "The confirm password field is required",
            'error_messages': "The confirm password and new password must match",
            'min_value': "The confirm password should contains at least 8 digits",
        }
    )