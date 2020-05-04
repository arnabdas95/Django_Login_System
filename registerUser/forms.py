from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Extra

#inherited from the UserCreationForm
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#this form is for an extra field in user register or login time
class ExtraForm(forms.ModelForm):
    class Meta():
        model = Extra
        fields = ('extra_field',)

