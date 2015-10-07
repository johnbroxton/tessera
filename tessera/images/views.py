from django.shortcuts import render
from PIL import Image
from django.http import HttpResponseRedirect
# from .forms import ImageForm
from .models import *

# Create your views here.

def images(request):
    form = Image()
    if request.method == "POST":
        form = Image()
        form.file = request.FILES['new_image']
        form.save()

    return render(request, 'index.html', {'form':form})


