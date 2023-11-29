from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from .task import Deposit_maker
from .models import Plan
def Email_sender(request):
    if request.method=='GET':
        return render(request,'ded.html',{})
    else:
        return redirect('/')
