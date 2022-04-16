from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets 
from django.contrib.auth.forms import UserCreationForm  
from .models import Cat, Dog 

# class SignupForm(UserCreationForm):
#     fullname = forms.CharField(max_length=50)

#     class Meta:
#         model = JangsaUser
#         fields = ('fullname', 'username', 'phone_number', 'email', 'password1', 'password2')


# class JangsaUserForm(ModelForm):

#      fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'class': "form-control", 'placeholder': 'Full name', 'required':'', 
         
#     }))
     
#      username = forms.CharField()(widget=forms.TextInput(attrs={
#         'class': "form-control", 'placeholder': 'Username', 'required':'',
        
#     })) 
#      phone_number = forms.ImageField()(wdgets =forms.NumberInput(attrs ={
#         'class': "form-control", 'placeholder':'Phone number', 'required':'', 'pattern': '[1][7][0-9]{6}'
#     }))

#      email = forms.EmailField(widget=forms.EmailInput(attrs={
#         'class': "form-control", 'placeholder': 'Email Address', 'required':'',

#     })) 
#      password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': "form-control", 'id':'pwd', 'placeholder': 'Password','required':'',

#     }))

#      password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': "form-control", 'id':'pwd', 'placeholder': 'Confirm Password', 'required':'',

#     })) 




class CatForm(ModelForm):

    class Meta:
        model = Cat
        fields = [ "name","image","age","description"] 


class DogForm(ModelForm):
    
    class Meta:
        model = Dog 
        fields = [ "name","image","age","description"] 


# class UserForm(forms.ModelForm):
