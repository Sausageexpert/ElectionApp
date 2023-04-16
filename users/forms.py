from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'emailClass'}), label = '')
    ID = forms.CharField(widget = forms.TextInput(attrs={'class':'emailClass'}), label = '')
    class Meta():
        model=User
        fields=['name','ID']