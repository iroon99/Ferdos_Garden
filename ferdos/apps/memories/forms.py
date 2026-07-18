from django import forms
from .models import MemoryGallery, Memory

class MemoryGalleryForm(forms.ModelForm):
    class Meta:
        model = MemoryGallery
        fields = [
            'memory_image'
        ]
    
class MemoryForm(forms.ModelForm):
    # Define Widgets
    memory_title = forms.CharField(label='عنوان خاطره', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان خاطراه را وارد کنید'}))
    memory_text = forms.CharField(label='متن خاطره', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'متن خاطراه را وارد کنید'}))

    class Meta:
        model = Memory
        fields = [
            'memory_title',
            'memory_text'
        ]
    
        
        