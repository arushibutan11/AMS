from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .models import details, injured, killed
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.forms.formsets import formset_factory


class FirForm(forms.ModelForm):
    DATE_OCC = forms.DateField(required = False,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 1, datetime.date.today().year + 10)),
        )
    dri_lic_date_issu= forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    dri_lic_date_upto= forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    CONVERT_DATE=forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
        )
    BRIEF_FACTS = forms.CharField( required = False, widget=forms.Textarea)
    REMARK = forms.CharField( required = False, widget=forms.Textarea)
    class Meta:
        model = details
     	fields=['ACC_ID','RNG','CIRCLE','DIST','PS','FIRNO','SECTION','TIME_OCC','TIME_TYPE', 'DATE_OCC',
 'PLACE_OCC','ROAD', 'ROADNAME', 'LOCATION','CATEGORY', 'VEHTYPE1', 'TWW1', 'RNOV1A', 'RNOV1B', 
 'VEHTYPE2', 'TWW2', 'RNOV2A', 'RNOV2B', 'SELF_TYPE', 'INJURED', 'INJMALE','INJFEMALE', 'INJBOY',
 'INJGIRL', 'KILLED', 'KILMALE', 'KILFEMALE', 'KILBOY', 'KILGIRL', 'PEDESTRIAN', 'ACCTYPE',
'ACCID_TYPE','VICTIM', 'DUPL', 'PENDING','DAY_NIGHT','YEAR','TIME_SLOT', 'MONTH','FN','ACCAGE','ACCSEX',
'ACCDRUNK' , 'Intersection', 'routeno', 'case_status','convert_case', 'BRIEF_FACTS' ,'dri_lic_no', 
'dri_name', 'dri_fath', 'dri_sex','dri_age','dri_add','dri_arrest','dri_place','dri_lic_date_issu',
'dri_lic_date_upto', 'dri_lic_status','REMARK', 'CONFIRM', 'LONGITUDE', 'LATITUDE', 'CONVERT',
'CONVERT_DATE', 'CN_DT', 'CONVERT_FN','BUS_NO', 'BLACK_SPOT', 'BLACK_SPOT_NO', 'FOR_BLK', 'STATUS',
 'F_STATUS','dri_add1','RIDER_HELMET', 'PILLION_HELMET', 'STATE', 'SCANNED', 'HIT_AND_RUN_UPDATE1']
 
 
    def clean(self):
        cd = self.cleaned_data
        if cd.get('dri_lic_date_issu') > cd.get('dri_lic_date_upto'):
            self.add_error('dri_lic_date_upto', "Driver License Validity cannot be before Issued Date")
            
        if cd.get('LATITUDE') > 29 or cd.get('LATITUDE') <= 28:
             self.add_error('LATITUDE', "Check Value of Latitude")
             
        if cd.get('LONGITUDE') >= 78 or cd.get('LONGITUDE') < 76:
             self.add_error('LONGITUDE', "Check Value of Longitude") 
             
        tim1 = cd.get('TIME_OCC')[:2]
        tim2 = cd.get('TIME_OCC')[-2:]
        tim1 = int(tim1)
        tim2 = int(tim2)
        if tim1 > 23 or tim1 < 0 or tim2 > 59 or tim2 < 0:
            self.add_error('TIME_OCC', "Enter a valid time")
        return cd          
        '''VEHTYPE2 = cd.get('VEHTYPE2')
        VICTIM = cd.get('VICTIM')

        if VEHTYPE2 == "PEDESTRIAN" and (VICTIM == "VEHICLES" or VICTIM == "SELF" or VICTIM == "PASSENGER" or VICTIM == "SELF/ANIMAL"):
            self.add_error('VICTIM', "Victim is Pedestrian")        
        elif VEHTYPE2 == "SELF" and (VICTIM == "PEDESTRIAN" or VICTIM == "PASSENGER" or VICTIM == "VEHICLES" or VICTIM == "VEHICLES/PED"):
            self.add_error('VICTIM', "Victim is Self")
        elif VEHTYPE2 == "ANIMAL" and (VICTIM == "SELF" or VICTIM == "PEDESTRIAN" or VICTIM == "PASSENGER" or VICTIM == "VEHICLES" or VICTIM == "VEHICLES/PED"):
            self.add_error('VICTIM', "Victim is self/animal")
        elif VEHTYPE2 == "PASSENGER" and (VICTIM == "SELF" or VICTIM == "PEDESTRIAN" or VICTIM == "SELF/ANIMAL" or VICTIM == "VEHICLES" or VICTIM == "VEHICLES/PED"):
            self.add_error('VICTIM', "Victim is passenger")
        elif (VEHTYPE2 != "SELF" and VEHTYPE2 != "PASSENGER" and VEHTYPE2 != "PEDESTRIAN" and VEHTYPE2 != "ANIMAL") and (VICTIM == "PEDESTRIAN" or VICTIM == "PASSENGER" or VICTIM == "SELF" or VICTIM == "SELF/ANIMAL"):
            self.add_error('VICTIM', "Victim is vehicle")'''





class InjForm(forms.ModelForm):
	class Meta:
 		model = injured
 		fields = ['INJSEX', 'INJAGE', 'INJTYPE', 'PS', 'YEAR', 'ACCID_ID', 'FIRNO']

class KilForm(forms.ModelForm):
	class Meta:
 		model = killed
 		fields = ['SEX', 'AGE', 'TYPE', 'PS', 'YEAR', 'ACCID_ID', 'FIRNO']
    