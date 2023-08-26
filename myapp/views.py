from django.shortcuts import render
from .models import Image
from .forms import imageform

# Create your views here.
def image_upload(request):
    if request.method=='POST':
        fm=imageform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=imageform()
    else:
        fm=imageform()
    img=Image.objects.all()
    return render(request,'myapp/home.html', {'form':fm,'img':img})
    
    
