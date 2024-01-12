from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name:'})
    ) 
    last_name= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name:'})
    ) 
    email= forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email:'})
    ) 
    username= forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username:'})
    ) 
    password1= forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'It should be at least 8 Characters'
            }
        )
    )
    password2= forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Reenter your password'
            }
        )
    )

    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')