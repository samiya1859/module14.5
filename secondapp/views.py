from django.shortcuts import render
from secondapp.forms import UserForm
# Create your views here.

def contact(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            return render(request,'userform2.html',{'form':form})
    else:
        form = UserForm()        
    return render(request,'userform2.html',{'form':form})