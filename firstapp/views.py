from django.shortcuts import render,redirect
from . forms import UserForm

# Create your views here.

def contact(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'userform.html',{'form':form})
    else:
        form=UserForm()
    
    return render(request,'userform.html',{'form':form})
