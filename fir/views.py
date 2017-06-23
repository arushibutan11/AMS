# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details, circles, sections, injured, killed, location, accid_type
from .forms import FirForm, InjForm, KilForm
from django.forms import ModelForm
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
import json

# Create your views here.
def create_fir(request):
    InjFormSet = modelformset_factory(injured, fields = ('PS', 'FIRNO', 'YEAR', 'INJAGE','INJSEX','INJTYPE', 'ACCID_ID'), widgets = {
    'PS': forms.TextInput(attrs={'class': 'iPS cloned injcloned'}),'FIRNO': forms.TextInput(attrs={'class': 'iFIRNO cloned injcloned'}), 
    'YEAR': forms.TextInput(attrs={'class': 'iYEAR cloned injcloned'}),'ACCID_ID': forms.TextInput(attrs={'class': 'iACCID_ID cloned injcloned'}),},
    formset=InjForm)
    
    KilFormSet = modelformset_factory(killed, fields = ('PS', 'FIRNO', 'YEAR', 'AGE','SEX','TYPE','ACCID_ID' ), widgets = {
    'PS': forms.TextInput(attrs={'class': 'iPS cloned kilcloned'}),'FIRNO': forms.TextInput(attrs={'class': 'iFIRNO cloned kilcloned'}), 
    'YEAR': forms.TextInput(attrs={'class': 'iYEAR cloned kilcloned'}),'ACCID_ID': forms.TextInput(attrs={'class': 'iACCID_ID cloned kilcloned'}),},
    formset=KilForm)
    
    if request.method == 'POST':

      form = FirForm(request.POST)
      injform = InjFormSet(request.POST)
      kilform = KilFormSet(request.POST)

      CNTM = 0
      CNTF = 0
      CNTB = 0
      CNTG = 0
      CNTMI = 0
      CNTFI = 0
      CNTBI = 0
      CNTGI = 0
      if form.is_valid():

        if form.data['ACCTYPE'] == 'F' and kilform.is_valid():
            fir = form.save(commit = False)
            cd = form.cleaned_data
            ACCID_ID = cd.get('ACCID')

            for k in kilform:
              kd = k.cleaned_data
              sex = kd.get('SEX')
              age = kd.get('AGE')
              accid = kd.get('ACCID_ID')
              print accid
              if (sex == "M") and (age == "<10"):
                CNTB = CNTB + 1
              elif (sex == "F") and (age == "<10"):
                CNTG = CNTG + 1
              elif (sex == "M"):
                CNTM = CNTM + 1
              elif (sex == "F"):
                CNTF = CNTF + 1
            KILLED =  CNTB + CNTG + CNTM + CNTF
            fir.KILLED = KILLED
            fir.KILMALE = CNTM
            fir.KILFEMALE = CNTF
            fir.KILBOY = CNTB
            fir.KILGIRL = CNTG
            kil = kilform.save()


            sec = form.data['SECTION']
            sec_obj = sections.objects.get(pk = sec)
            
            if ('338' in sec_obj.SECTIONDTL or '337' in sec_obj.SECTIONDTL) and injform.is_valid():
              for k in injform:
                kd = k.cleaned_data
                sex = kd.get('INJSEX')
                age = kd.get('INJAGE')
                if (sex == "M") and (age == "<10"):
                  CNTBI = CNTBI + 1
                elif (sex == "F") and (age == "<10"):
                  CNTGI = CNTGI + 1
                elif (sex == "M"):
                  CNTMI = CNTMI + 1
                elif (sex == "F"):
                  CNTFI = CNTFI + 1

              INJURED =  CNTBI + CNTGI + CNTMI + CNTFI
              fir.INJURED = INJURED
              fir.INJMALE = CNTMI
              fir.INJFEMALE = CNTFI
              fir.INJBOY = CNTBI
              fir.INJGIRL = CNTGI            
              inj = injform.save()
            fir.save()


        elif (form.data['ACCTYPE'] == 'S'  or form.data['ACCTYPE'] == 'G') and injform.is_valid():
            fir = form.save(commit =  False)
            for k in injform:
              kd = k.cleaned_data
              sex = kd.get('INJSEX')
              age = kd.get('INJAGE')
              if (sex == "M") and (age == "<10"):
                CNTB = CNTB + 1
              elif (sex == "F") and (age == "<10"):
                CNTG = CNTG + 1
              elif (sex == "M"):
                CNTM = CNTM + 1
              elif (sex == "F"):
                CNTF = CNTF + 1

              INJURED =  CNTBI + CNTGI + CNTMI + CNTFI
              fir.INJURED = INJURED
              fir.INJMALE = CNTM
              fir.INJFEMALE = CNTF
              fir.INJBOY = CNTB
              fir.INJGIRL = CNTG            
            fir.save()           
            inj = injform.save()

        elif form.data['ACCTYPE'] == 'N':
            fir = form.save()

        else:
            return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

        return HttpResponse('done')
      else:
        
        #return HttpResponse('validation done')
        return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

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
            
