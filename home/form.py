from django import forms
from .models import upload

class ImageForm(forms.ModelForm):
    class Meta:
        model=upload
        fields=("image","caption")
    
class ImageForm2(forms.ModelForm):
    class Meta:
        print("gsgfgfd")
        model=upload
        fields=("image","caption","news")