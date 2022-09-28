from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from . models import member
from .forms import member, memberform


# Create your views here.

def list(request):
    all_member = member.objects.all
    return render(request,'list.html',{'all' : all_member})

def join(request):
    if request.method=="POST":
        form = memberform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(request, ('There is an error...Try again'))
            return redirect('home')

        messages.success(request, ('Your Form Has Been Submited'))
        return redirect ('home')
    else:
        return render(request,'join.html',{})