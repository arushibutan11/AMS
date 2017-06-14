# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details
from .forms import FirForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_fir(request):
    #if not request.user.is_authenticated():
       # return render(request, 'music/login.html')
   # else:
    if request.method == 'POST':

      form = FirForm(request.POST)
      if form.is_valid():
        fir = form.save()
        
        return HttpResponse('done')
      else:
        return HttpResponse('done not')

    else:
        form = FirForm()
        return render(request,'details_form.html', { 'form': form})






