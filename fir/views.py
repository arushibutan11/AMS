# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details
from .forms import Form
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_fir(request):
    #if not request.user.is_authenticated():
       # return render(request, 'music/login.html')
   # else:
    form = Form(request.POST)
    if form.is_valid():
        fir = form.save(commit=False)
       # FIRNO = form.cleaned_data['FIRNO']
        #ACC_ID = form.cleaned_data['ACC_ID']
        #context=None
        return render(request,'details_form.html', {'fir': fir })

    else:
        return render(request,'details_form.html', { })



