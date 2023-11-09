from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from .models import Inventory_items

class Login_form(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email



class Signin_form(AuthenticationForm):
    class Meta:
        model = User
        fields  = ['username','password']
        

class EditForm(forms.ModelForm):
    class Meta:
             model = Inventory_items
             fields = ['item_name', 'quantity' ,'Unit_price','dispatched_from','dispatched_price'] 