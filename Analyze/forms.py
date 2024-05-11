from django import forms
from .models import FormData

class MyForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['field1', 'field2']