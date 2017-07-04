from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .models import details, injured, killed, profile, designation_choices, circle_choices, collision, offender, victim_person, victim_vehicle
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.forms.formsets import formset_factory
from django.forms.models import BaseModelFormSet, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required= True)
    emp_id = forms.CharField(max_length=15, required= True, label="Employee ID")
    circle = forms.ChoiceField(choices=circle_choices, widget=forms.Select(attrs={'class':'form-control'}), required= True)
    designation = forms.ChoiceField(choices=designation_choices, widget=forms.Select(attrs={'class':'form-control'}), required= True)


    class Meta:
        model = User
        fields = ('username', 'name', 'emp_id', 'circle', 'designation', 'password1', 'password2', )

    

class FirForm(forms.ModelForm):
    DATE_OCC = forms.DateField(required = False,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 1, datetime.date.today().year + 10)),
        )

    CONVERT_DATE=forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    BRIEF_FACTS = forms.CharField( required = False, widget=forms.Textarea)
    REMARK = forms.CharField( required = False, widget=forms.Textarea)
    file = forms.FileField()

    class Meta:
        model = details
     	exclude = ()
 

 
    def clean(self):
        cd = self.cleaned_data
        if cd.get('dri_lic_date_issu') > cd.get('dri_lic_date_upto'):
            self.add_error('dri_lic_date_upto', "Driver License Validity cannot be before Issued Date")
        if cd.get('LONGITUDE') != '': 
            LONGITUDE = float (cd.get('LONGITUDE'))
            if LONGITUDE >= 78.0 or LONGITUDE < 76.0:
                self.add_error('LONGITUDE', "Check Value of Longitude")             
        if cd.get('LONGITUDE') != '':
            LATITUDE = float  (cd.get('LATITUDE'))  
            if LATITUDE > 29.0 or LATITUDE <28.0:
                self.add_error('LATITUDE', "Check Value of Latitude")             

             
        if cd.get('TIME_OCC') is not "UNK":
            tim1 = cd.get('TIME_OCC')[:2]
            tim2 = cd.get('TIME_OCC')[-2:]
            tim1 = int(tim1)
            tim2 = int(tim2)
            if (tim1 > 23 or tim1 < 0 or tim2 > 59 or tim2 < 0):
                self.add_error('TIME_OCC', "Enter a valid time")

        VEHTYPE2 = str(cd.get('VEHTYPE2'))        
        VICTIM = str(cd.get('VICTIM'))

        if ("PEDESTRIAN" in VEHTYPE2) and ("VEHICLES" in VICTIM or "SELF"  in VICTIM or "PASSENGER"  in VICTIM or "SELF/ANIMAL" in VICTIM ):
            self.add_error('VICTIM', "Victim is Pedestrian")        
        elif (VEHTYPE2 == "SELF") and ("PEDESTRIAN" in VICTIM or "PASSENGER" in VICTIM  or "VEHICLES" in VICTIM or "VEHICLES/PED" in VICTIM ):
            self.add_error('VICTIM', "Victim is Self")
        elif ("ANIMAL" in VEHTYPE2) and (VICTIM == "SELF" or "PEDESTRIAN" in VICTIM or "PASSENGER" in VICTIM or "VEHICLES" in VICTIM or "VEHICLES/PED" in VICTIM ):
            self.add_error('VICTIM', "Victim is self/animal")
        elif ("PASSENGER" in VEHTYPE2) and ("SELF" in VICTIM  or "PEDESTRIAN" in VICTIM  or "SELF/ANIMAL" in VICTIM  or "VEHICLES" in VICTIM or "VEHICLES/PED" in VICTIM ):
            self.add_error('VICTIM', "Victim is passenger")
        elif ("SELF" not in VEHTYPE2 and "PASSENGER" not in VEHTYPE2 and "PEDESTRIAN" not in VEHTYPE2  and "ANIMAL" not in VEHTYPE2 ) and ("PEDESTRIAN" in VICTIM  or "PASSENGER" in VICTIM  or "SELF" in VICTIM  or "SELF/ANIMAL" in VICTIM):
            self.add_error('VICTIM', "Victim is vehicle")       
        return cd          

class OffendForm(forms.ModelForm):
    dri_lic_date_issu= forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    dri_lic_date_upto= forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    class Meta:
        model = offender
        exclude = ('ACCID_ID',)

class VVicForm(forms.ModelForm):

    class Meta:
        model = victim_vehicle
        exclude = ('ACCID_ID',)

class PVicForm(forms.ModelForm):

    class Meta:
        model = victim_person
        exclude = ('ACCID_ID',)

class CollisionForm(forms.ModelForm):

    class Meta:
        model = collision
        exclude = ('ACCID_ID',)

class InjForm(forms.ModelForm):

    class Meta:
        model = injured
        exclude = ('ACCID_ID',)
    '''def __init__(self, *args, **kwargs):
        super(InjForm, self).__init__(*args, **kwargs)
        self.queryset = injured.objects.none()'''
   



class KilForm(forms.ModelForm):
    class Meta:
        model = killed
        exclude = ('ACCID_ID',)
    '''def __init__(self, *args, **kwargs):
        super(KilForm, self).__init__(*args, **kwargs)
        self.queryset = killed.objects.none()'''