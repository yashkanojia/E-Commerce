from django import forms
from django.forms import ModelForm, widgets
from core.models import profile,product_category,products
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    captcha = CaptchaField()


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    file= forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}))
    captcha = CaptchaField()

    class Meta:
        model = profile
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2', 'is_seller','file')

class ProductForm(ModelForm):
    class Meta:
        model=products
        fields=['Product_title','Brand','Product_mrp','Selling_price','category_id','Product_description','Quantity_available','Country_of_origin','Product_image','Product_image_2']


class SecondStepVerificationForm(forms.Form):
    OTP = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class ProfileForm(ModelForm):
    
    class Meta:
        model = profile
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code')