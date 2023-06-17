
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import *
from django import forms

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    class Meta:
        model = myuser
        fields = ('email','first_name','last_name','password1','password2')



class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'type': 'email'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'type': 'password'}))

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct Email and password for a customer's account. Note that both fields are case-sensitive."
        ),
    }

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_customer:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username':self.username_field.verbose_name}
            )


   




class CustomerCreationForm(UserCreationForm):
    
    class Meta:
        model = myuser
        fields= ('email', 'first_name', 'last_name', 'password1', 'password2')


    def save(self, commit=True):
        user= super().save(commit=True)
        user.is_customer = True
        user.is_active =True

        if commit:
            user.save()

        return user



class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        fields = '__all__'

class EditUser(forms.ModelForm):
    class Meta:
        model = myuser
        fields = ['first_name','last_name',]





PAYMENT =(
    ('P', 'Paystack'),
    ('C', 'Crypto')
)

DeliveryMethod =(
    ('D', 'Door Delivery'),
    ('P', 'Pickup Station(Cheaper Shipping Fees than Door Delivery')
)

class CheckoutForm(forms.Form):
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT)
    delivery_method = forms.ChoiceField(widget=forms.RadioSelect, choices=DeliveryMethod)


#sellers


class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'type': 'email'}))
    password = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'type': 'password'}))

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct Email and password for a seller's account. Note that both fields are case-sensitive."
        ),
    }

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_seller:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username':self.username_field.verbose_name}
            )




class SellerCreationForm(UserCreationForm):
    
    class Meta:
        model = myuser
        fields= ('email', 'first_name', 'last_name', 'password1', 'password2')


    def save(self, commit=True):
        user= super().save(commit=True)
        user.is_seller = True
        user.is_active =True

        if commit:
            user.save()

        return user


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

class  ProductForm(forms.ModelForm):
    class Meta:
        model =  Product
        fields = '__all__'