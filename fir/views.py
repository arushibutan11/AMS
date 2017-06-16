# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details, circles, sections
from .forms import FirForm
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
import json



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


@permission_classes((permissions.AllowAny,))
def getcircleinfo(request):
  
    if request.method == 'POST':
      circle = request.POST.get('circle')
      info = circles.objects.get(CIRCLENAM = circle)
      return HttpResponse(json.dumps(info.as_json()), content_type="application/json")
            


@permission_classes((permissions.AllowAny,))
def getsection(request):
  
    if request.method == 'POST':
      section = request.POST.get('section')
      info = sections.objects.get(SECTIONDTL = section)
      return HttpResponse(json.dumps(info.as_json()), content_type="application/json")

