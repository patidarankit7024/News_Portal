from django import forms
from .models import upload

class ImageForm(forms.ModelForm):
    class Meta:
        model=upload
        fields=("image","caption")
    
