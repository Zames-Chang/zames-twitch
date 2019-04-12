from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from user.models import User 
from user.utils.account import Account
import logging
import sys

# Create your views here.
"""
def register(request):
    if request.method == 'POST':
        user = User()
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
        else:
            return render(request,'registration/register.html',{'form':form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
"""
def register(request):
    if request.method == 'POST':
        accout = Account(request.POST['account'],request.POST['password1'],request.POST['password2'])
        x = accout.is_valid()
        logging.error(x)
        return render(request, 'registration/register.html')
    else:
        return render(request, 'registration/register.html')