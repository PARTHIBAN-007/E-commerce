from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class customeruserform(UserCreationForm):
    
    contactnumber = forms.RegexField(regex=r'^\d{10]$',max_length=10,required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Contact Number','no-spinners':'no-spinners'}))
    class Meta:
        model=User
        fields=['username','email']
        widgets={
           'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
           'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'})
        }