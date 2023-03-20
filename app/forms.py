from django import forms
from app.models import blood
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class addmyform(forms.ModelForm):
    class Meta:
        model=blood
        fields='__all__'

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
     















'''
class myform(forms.ModelForm):
    class Meta:
        model=signupform
        fields='__all__'
        '''