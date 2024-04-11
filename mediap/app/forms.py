from django import forms
from app.models import*

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Rform
        fields='__all__'