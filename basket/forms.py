from django import forms
from basket.models import BasketModel

class BasketForm(forms.ModelForm):
    class Meta:
        model = BasketModel
        fields = '__all__'