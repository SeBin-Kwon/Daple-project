from django import forms
from .models import Store

class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ['store_name', 'store_address', 'store_tel', 'store_image']

