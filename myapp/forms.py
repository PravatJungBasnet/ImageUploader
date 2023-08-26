from .models import Image
from django  import forms
class imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields=['title','image']
       
   