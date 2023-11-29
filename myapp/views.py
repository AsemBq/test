from django.shortcuts import render,redirect,reverse
from django.views import View
from .task import test_func
from send_mail.models import Plan
from send_mail.task import Deposit_maker


class bib(View):
    def get(self,request):
        return render(request,'bib.html')

    def post(self,request):
        # Deposit_maker.delay()
        return redirect(reverse('test:em'))
