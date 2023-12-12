from django import forms
from .models import Xray

class XrayForm(forms.ModelForm):
    class Meta:
        model = Xray
        fields = ['name', 'image']