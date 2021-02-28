from django import forms
from .models import item,shop

class itemsform(forms.ModelForm):
    class Meta:
        model = item
        fields = ["itemname", "quantity"]
class shopform(forms.ModelForm):
    class Meta:
        model = shop
        fields = ["itemname", "quantity","stock"]