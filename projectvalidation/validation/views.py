from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm


# Create your views here.
def validation(request):
    return HttpResponse("new validation")
def home_view(request):
    if request.method=='POST':
        user_details=UserForm(request.POST)
        if user_details.is_valid():
            user_details.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request,'home.html',{'form':user_details})
    else:
        form=UserForm(None)
        return render(request,'home.html',{'form':form})
