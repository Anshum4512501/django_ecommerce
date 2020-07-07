from django.forms import ModelForm,Textarea,TextInput
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'zipcode']
        widgets = {
            'address': Textarea(attrs={'cols': 80, 'rows': 2,'class': 'form-control', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'state': TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}),
            'zipcode': TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}),
        }
       