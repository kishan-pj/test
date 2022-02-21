from django import forms
from .models import *


class ProductForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class BookingForms(forms.ModelForm):
    class Meta:
        model = Cartproducts
        fields = "__all__"


class Seeorders(forms.ModelForm):
    class Meta:
        model = Seeorder
        fields = "__all__"
