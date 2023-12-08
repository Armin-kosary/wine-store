from django import forms
from .models import Order


class CompletePurchaseForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='First Name', widget=forms.TextInput(attrs={
        'type' : 'text',
        'id' : 'firstName',
        'name' : 'firstName'
    }))
    last_name = forms.CharField(max_length=200, label='Last name',widget=forms.TextInput(attrs={
        'type' : 'text',
        'id' : 'lastName',
        'name' : 'lastName'
    }))
    address = forms.CharField(max_length=200, label='Adress',widget=forms.TextInput(attrs={
        'type' : 'text',
        'id' : 'address',
        'name' : 'address'
    }))
    phone = forms.CharField(label='Phone number', widget=forms.NumberInput(attrs={
        'type' : 'number',
        'id' : 'phoneNumber',
        'name' : 'phoneNumber'
    }))


    # class Meta:
    #     model = Order
    #     fields = '__all__'
    #     exclude = ['products']

    #     labels = {
    #         'first_name' : 'First Name',
    #         'last_name' : 'Last Name',
    #         'address' : 'Adress',
    #         'phone' : 'Phone number',

    #     }

    #     widgets = {
    #         'first_name' : forms.TextInput(attrs = {
    #             'type' : 'text',
    #             'id' : 'firstName',
    #             'name' : 'firstName'
    #         }),
    #         'last_name' : forms.TextInput(attrs = {
    #             'type' : 'text',
    #             'id' : 'lastName',
    #             'name' : 'lastName'
    #         }),
    #         'address' : forms.TextInput(attrs = {
    #             'type' : 'text',
    #             'id' : 'firstName',
    #             'name' : 'firstName'
    #         }),
    #         'phone' : forms.NumberInput(attrs = {
    #             'type' : 'text',
    #             'id' : 'phoneNumber',
    #             'name' : 'phoneNumber'
    #         })


    #     }
