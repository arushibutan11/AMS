# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import details, circles, sections, injured, killed, location, accid_type, offender, collision, victim_person, victim_vehicle
from .forms import FirForm, InjForm, KilForm, SignUpForm, PVicForm, VVicForm, OffendForm, CollisionForm, CauseForm
from django.forms import ModelForm
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory
from django.db.models import Q
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin, authenticate
from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm
from .models import profile
import urllib
import urllib2
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
import re
from django.contrib import messages


@user_passes_test(lambda user: not user.username, login_url=settings.LOGIN_REDIRECT_URL, redirect_field_name=None) #whatdoesthisdo
def login(request):
  print "inside req"
  if request.method=='POST':
      name = request.POST.get('name', None)
      pwd = request.POST.get('pwd', None)
      if ( pwd is '' or name is '' ):
          messages.error(request, "Fill in all the fields.")
      else:

          user = authenticate(username=name, password=pwd)
          if user is not None:
            if user.is_active:
                  authlogin(request, user)
                  print "after authlogin"
                  return redirect('home')
            else:
                  messages.error(request, "Your account is disabled. Please contact the system administrator.")
          else:
                  messages.error(request, "Invalid Username or Password")


  return render(request, 'login.html')


def log_end(request):
    logout(request)
    return HttpResponseRedirect('logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            user.profile.name = form.cleaned_data.get('name')
            user.profile.emp_id = form.cleaned_data.get('emp_id')
            user.profile.circle = form.cleaned_data.get('circle')
            user.profile.designation = form.cleaned_data.get('designation')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            authlogin(request, user)
            user.refresh_from_db()
            if (user.profile.designation == 'DCP'):
                g = Group.objects.get(name='dcp')
                g.user_set.add(user)
            if (user.profile.designation == 'ACP'):
                g = Group.objects.get(name='acp')
                g.user_set.add(user)
            if (user.profile.designation == 'INS'):
                g = Group.objects.get(name='ins')
                g.user_set.add(user)
            if (user.profile.designation == 'ARC'):
                user.is_superuser = True
                user.is_staff = True
                user.save()
                g = Group.objects.get(name='arc')
                g.user_set.add(user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    if (request.user.groups.filter(name='arc').exists() == 1):
        isadmin = True
    else:
        isadmin = False
    return render(request, 'home.html', {'isadmin': isadmin})

@login_required(login_url=settings.LOGIN_URL)
def create_fir(request):
    InjInlineFormSet = inlineformset_factory(details, injured, fields = ('PS', 'FIRNO', 'YEAR', 'INJAGE','INJSEX','INJTYPE'), widgets = {
    'PS': forms.TextInput(attrs={'class': 'iPS cloned injcloned'}),'FIRNO': forms.TextInput(attrs={'class': 'iFIRNO cloned injcloned'}),
    'YEAR': forms.TextInput(attrs={'class': 'iYEAR cloned injcloned'}),},
    form=InjForm, extra = 1)

    KilInlineFormSet = inlineformset_factory(details, killed, fields = ('PS', 'FIRNO', 'YEAR', 'AGE','SEX','TYPE'),
      widgets = {'PS': forms.TextInput(attrs={'class': 'iPS cloned kilcloned'}),
      'FIRNO': forms.TextInput(attrs={'class': 'iFIRNO cloned kilcloned'}),
      'YEAR': forms.TextInput(attrs={'class': 'iYEAR cloned kilcloned'}),},
      form=KilForm, extra = 1)


    if request.method == 'POST':

      form = FirForm(request.POST,request.FILES)
      injform = InjInlineFormSet(request.POST, prefix = 'injured')
      kilform = KilInlineFormSet(request.POST, prefix = 'killed')
      if form.is_valid():
        fir = form.save()
        injform = InjInlineFormSet(request.POST, request.FILES, instance=fir, prefix = 'injured')
        kilform = KilInlineFormSet(request.POST, request.FILES, instance=fir, prefix = 'killed')
        cd = form.cleaned_data
        firid = str(cd.get('ACC_ID'))

        if form.data['ACCTYPE'] == 'F':
          if kilform.is_valid():
            kil = kilform.save()
            count_kil(firid)
            sec = form.data['SECTION']
            sec_obj = sections.objects.get(pk = sec)

            if ('338' in sec_obj.SECTIONDTL or '337' in sec_obj.SECTIONDTL):
              if injform.is_valid():
                inj = injform.save()
                count_inj(firid)
              #Injform is invalid and Kilform is valid
              else:
                return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})
          else:
            #If Kilform is invalid
            return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

        elif (form.data['ACCTYPE'] == 'S'  or form.data['ACCTYPE'] == 'G'):
          if injform.is_valid():
            count_inj(firid)
            inj = injform.save()
          else:
            # If Injform is invalid
            return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

        elif form.data['ACCTYPE'] == 'N':
            pass

        else:
            return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

        return HttpResponseRedirect('/fir/edit_fir/'+str(fir.ACC_ID)+'/')
      else:
        #if main form is not Valid
        return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

    #If method is not POST
    else:
        form = FirForm()
        injform = InjInlineFormSet(prefix = 'injured')
        kilform = KilInlineFormSet(prefix = 'killed')
        return render(request,'details_form.html', { 'form': form, 'forminj': injform, 'formkil':kilform})

@user_passes_test(lambda u: u.groups.filter(name='arc').exists() == 1, login_url=settings.LOGIN_REDIRECT_URL)
@login_required(login_url=settings.LOGIN_URL)
def edit_fir(request,acc_id):
    PVicInlineFormSet = inlineformset_factory(details, victim_person, exclude = (), form=PVicForm, extra = 0)
    VVicInlineFormSet = inlineformset_factory(details, victim_vehicle, exclude = (), form=VVicForm, extra = 0)
    OffendInlineFormSet = inlineformset_factory(details, offender, exclude = (), form=OffendForm, extra = 0)
    fir = get_object_or_404(details, pk = acc_id)

    if request.method == 'POST':
      pvicform = PVicInlineFormSet(request.POST, prefix = 'pvic',instance = fir)
      vvicform = VVicInlineFormSet(request.POST, prefix = 'vvic', instance = fir)
      offendform = OffendInlineFormSet(request.POST, prefix = 'offend', instance = fir)
      collisionform = CollisionForm(request.POST, prefix = 'collision', instance =  fir)
      form = FirForm(request.POST,request.FILES, instance = fir)
      form2 = CauseForm(request.POST,request.FILES,instance=fir)
      if form.is_valid():
        fir = form.save()
        if (not form2.is_valid()) or (not pvicform.is_valid()) or (not vvicform.is_valid()) or (not offendform.is_valid()) or (not collisionform.is_valid()):
            return render(request,'edit_form.html', { 'fir': fir, 'form2': form2, 'form': form, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})

        else:
          pvicform.save()
          vvicform.save()
          offendform.save()
          collisionform.save()
          form2.save()
          return HttpResponse('done')
      else:
        return render(request,'edit_form.html', { 'fir': fir, 'form': form, 'form2':form2, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})


    else:
        form = FirForm(instance = fir)
        pvicform = PVicInlineFormSet(prefix = 'pvic', instance = fir)
        vvicform = VVicInlineFormSet(prefix = 'vvic', instance = fir)
        offendform = OffendInlineFormSet(prefix = 'offend', instance = fir)
        collisionform = CollisionForm(request.POST, request.FILES, prefix = 'collision', instance =  fir)
        return render(request,'edit_form.html', { 'fir': fir, 'form': form, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})



@login_required(login_url=settings.LOGIN_URL)
def new_fir(request):
    PVicInlineFormSet = inlineformset_factory(details, victim_person, exclude = (), form=PVicForm, extra = 1)
    VVicInlineFormSet = inlineformset_factory(details, victim_vehicle, exclude = (), form=VVicForm, extra = 1,max_num= 4)
    OffendInlineFormSet = inlineformset_factory(details, offender, exclude = (), form=OffendForm, extra = 1,max_num= 3)

    if request.method == 'POST':
      form = FirForm(request.POST,request.FILES)
      form2 = CauseForm(request.POST,request.FILES)

      pvicform = PVicInlineFormSet(request.POST, prefix = 'pvic')
      vvicform = VVicInlineFormSet(request.POST, prefix = 'vvic')
      offendform = OffendInlineFormSet(request.POST, prefix = 'offend')
      collisionform = CollisionForm(request.POST, prefix = 'collision')

      if form.is_valid():
        fir = form.save()
        fir.MONTH = fir.DATE_OCC.month
        if (fir.DATE_OCC.day <= 15):
            fir.FN = 1
        else:
            fir.FN = 2

        form2 = CauseForm(request.POST,request.FILES, instance=fir)
        pvicform = PVicInlineFormSet(request.POST, request.FILES, instance=fir, prefix = 'pvic')
        vvicform = VVicInlineFormSet(request.POST, request.FILES, instance=fir, prefix = 'vvic')
        offendform = OffendInlineFormSet(request.POST, request.FILES, instance=fir, prefix = 'offend')
        collisionform = CollisionForm(request.POST, request.FILES, prefix = 'collision', instance =  fir)
        if vvicform.is_valid() and offendform.is_valid():
            offendform.save()
            vvicform.save()
            if (not form2.is_valid())or (not pvicform.is_valid()) or (not collisionform.is_valid()):
                return render(request,'new_form.html', { 'form': form, 'form2':form2, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})
            else:
              form2.save()
              pvicform.save()
              collisionform.save()
              return HttpResponse('done')
        else:
            return render(request,'new_form.html', { 'form': form, 'form2':form2, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})
      else:
        return render(request,'new_form.html', { 'form': form, 'form2':form2, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})


    else:
        form = FirForm()

        form2 = CauseForm()
        pvicform = PVicInlineFormSet(prefix = 'pvic')
        vvicform = VVicInlineFormSet(prefix = 'vvic')
        offendform = OffendInlineFormSet(prefix = 'offend')
        collisionform = CollisionForm(prefix = 'collision')
        return render(request,'new_form.html', { 'form': form, 'form2':form2, 'vvicform' :vvicform,'pvicform' :pvicform,'offendform' :offendform,'collisionform' :collisionform})




def report_acc_type(request, month, year, fn):
    #OF_SECTION.ACCTYPE
    year = int(year)
    month = int(month)
    fn = int(fn)
    monthfn = details.objects.filter(MONTH = month, FN = fn)
    noninjury = details.objects.filter(OF_SECTION__ACCTYPE = 'N', MONTH = month, FN = fn)
    simple = details.objects.filter(OF_SECTION__ACCTYPE = 'S', MONTH = month, FN = fn)
    fatal = details.objects.filter(OF_SECTION__ACCTYPE = 'F', MONTH = month, FN = fn)

    acc_type=[]
    rowcur = []
    rowcur.append(year)
    rowcur.append(noninjury.filter(DATE_OCC__year = year).count())
    rowcur.append(simple.filter(DATE_OCC__year = year).count())
    rowcur.append(fatal.filter(DATE_OCC__year = year).count())
    rowcur.append(rowcur[1]+rowcur[2]+rowcur[3])
    rowprev=[]
    rowprev.append(year-1)
    rowprev.append(noninjury.filter(DATE_OCC__year = year-1).count())
    rowprev.append(simple.filter(DATE_OCC__year = year-1).count())
    rowprev.append(fatal.filter(DATE_OCC__year = year-1).count())
    rowprev.append(rowprev[1]+rowprev[2]+rowprev[3])
    acc_type.append(rowcur)
    acc_type.append(rowprev)

    daynight=[]
    row=[]
    row.append(day)
    row.append()
    daynight.append(row)
    night=[]
    unknown=[]

    
    return render(request, 'report_acc_type.html', { 'acc_type': acc_type})

'''def count_inj(firid):
    is_fir = Q(ACCID_ID = firid)
    is_male = Q(INJSEX = "F")
    is_female = Q(INJSEX = "M")
    is_minor = Q(INJAGE = "<10")
    CNTB = injured.objects.filter(is_fir & is_male & is_minor).count()
    CNTG = injured.objects.filter(is_fir & is_female & is_minor).count()
    CNTM = injured.objects.filter(is_fir & is_male & ~(is_minor)).count()
    CNTF = injured.objects.filter(is_fir & is_female & ~(is_minor)).count()
    INJURED = CNTB + CNTG + CNTM + CNTF
    acc = details.objects.get(pk = firid)
    acc.INJURED = INJURED
    acc.INJMALE = CNTM
    acc.INJFEMALE = CNTF
    acc.INJBOY = CNTB
    acc.INJGIRL = CNTG
    if (acc.VEHTYPE2_id == "PED"):
      acc.PEDESTRIAN = acc.PEDESTRIAN +  INJURED
    acc.save()

def count_kil(firid):
    is_fir = Q(ACCID_ID = firid)
    is_male = Q(SEX = "M")
    is_female = Q(SEX = "F")
    is_minor = Q(AGE = "<10")
    CNTB = killed.objects.filter(is_fir & is_male & is_minor).count()
    CNTG = killed.objects.filter(is_fir & is_female & is_minor).count()
    CNTM = killed.objects.filter(is_fir & is_male & ~(is_minor)).count()
    CNTF = killed.objects.filter(is_fir & is_female & ~(is_minor)).count()
    KILLED = CNTB + CNTG + CNTM + CNTF
    acc = details.objects.get(pk = firid)
    acc.KILLED = KILLED
    acc.KILMALE = CNTM
    acc.KILFEMALE = CNTF
    acc.KILBOY = CNTB
    acc.KILGIRL = CNTG
    if (acc.VEHTYPE2_id == "PED"):
      acc.PEDESTRIAN = KILLED
    acc.save() '''
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):

    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@user_passes_test(lambda u: u.groups.filter(name='arc').exists() == 1, login_url=settings.LOGIN_REDIRECT_URL)
@login_required(login_url=settings.LOGIN_URL)
def search_fir(request):
    query_string = ''
    fir_entries = None


    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        fir_query = get_query(query_string, ['ACC_ID',])


        fir_entries = details.objects.filter(fir_query).order_by('-DATE_OCC')

    return render(request, 'search_fir.html', { 'query_string': query_string, 'fir_entries': fir_entries})


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
