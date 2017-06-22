# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details, circles, sections, injured, killed, location, accid_type
from .forms import FirForm, InjForm, KilForm
from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.forms.formsets import formset_factory
import json

# Create your views here.
def create_fir(request):
    InjFormSet = modelformset_factory(injured, fields = ('PS', 'FIRNO', 'YEAR', 'INJAGE','INJSEX','INJTYPE', 'ACCID_ID'), widgets = {
    'PS': forms.TextInput(attrs={'class': 'cloned injcloned'}),'FIRNO': forms.TextInput(attrs={'class': 'cloned injcloned'}), 
    'YEAR': forms.TextInput(attrs={'class': 'cloned injcloned'}),'ACCID_ID': forms.TextInput(attrs={'class': 'cloned injcloned'}),})
    KilFormSet = modelformset_factory(killed, fields = ('AGE','SEX','TYPE'))
    if request.method == 'POST':

      form = FirForm(request.POST)
      print request.POST.get("FIRNO")
      injform = InjFormSet(request.POST)
      kilform = KilFormSet(request.POST)
      if form.is_valid():
        if form.data['ACCTYPE'] == 'F' and injform.is_valid() and kilform.is_valid():
            fir = form.save()
            inj = injform.save()
            kil = kilform.save()  
        elif (form.data['ACCTYPE'] == 'S'  or form.data['ACCTYPE'] == 'G') and injform.is_valid():
            fir = form.save()
            inj = injform.save()
        elif form.data['ACCTYPE'] == 'N':
            fir = form.save()
        else:
            fir = form.save()

        return HttpResponse('done')
      else:
        
        return HttpResponse('validation done')
        #return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

    else:
        form = FirForm()
        injform = InjFormSet()
        kilform = KilFormSet()
        return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})


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

@permission_classes((permissions.AllowAny,))
def getlocation(request):
  
    if request.method == 'POST':
      loc = request.POST.get('location')
      info = location.objects.get(TYPE = loc)
      return HttpResponse(json.dumps(info.as_json()), content_type="application/json")

@permission_classes((permissions.AllowAny,))
def getacctype(request):
  
    if request.method == 'POST':
      acctype = request.POST.get('accid_type')
      info = accid_type.objects.get(SNO = acctype)
      return HttpResponse(json.dumps(info.as_json()), content_type="application/json")
            
