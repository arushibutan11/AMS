from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .models import details, injured, killed
from django.forms.extras.widgets import SelectDateWidget
import datetime


class FirForm(forms.ModelForm):
    DATE_OCC = forms.DateField(required=False, input_formats = settings.DATE_INPUT_FORMATS,
        widget=SelectDateWidget(years=range(datetime.date.today().year - 10, datetime.date.today().year + 10)),
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
    class Meta:
        model = details
     	fields=['ACC_ID','RNG','CIRCLE','DIST','PS','FIRNO','SECTION','TIME_OCC','TIME_TYPE',
 'PLACE_OCC','ROAD', 'ROADNAME', 'LOCATION','CATEGORY', 'VEHTYPE1', 'TWW1', 'RNOV1A', 'RNOV1B', 
 'VEHTYPE2', 'TWW2', 'RNOV2A', 'RNOV2B', 'SELF_TYPE', 'INJURED', 'INJMALE','INJFEMALE', 'INJBOY',
 'INJGIRL', 'KILLED', 'KILMALE', 'KILFEMALE', 'KILBOY', 'KILGIRL', 'PEDESTRIAN', 'ACCTYPE',
'ACCID_TYPE','VICTIM', 'DUPL', 'PENDING','DAY_NIGHT','YEAR','TIME_SLOT', 'MONTH','FN','ACCAGE','ACCSEX',
'ACCDRUNK' , 'Intersection', 'routeno', 'case_status','convert_case', 'BRIEF_FACTS' ,'dri_lic_no', 
'dri_name', 'dri_fath', 'dri_sex','dri_age','dri_add','dri_arrest','dri_place','dri_lic_date_issu',
'dri_lic_date_upto', 'dri_lic_status','REMARK', 'CONFIRM', 'LONGITUDE', 'LATITUDE', 'CONVERT',
'CONVERT_DATE', 'CN_DT', 'CONVERT_FN','BUS_NO', 'BLACK_SPOT', 'BLACK_SPOT_NO', 'FOR_BLK', 'STATUS',
 'F_STATUS','dri_add1','RIDER_HELMET', 'PILLION_HELMET', 'STATE', 'SCANNED', 'HIT_AND_RUN_UPDATE1']




class InjForm(forms.ModelForm):
	class Meta:
 		model = injured
 		fields = ['INJSEX', 'INJAGE', 'INJTYPE']

class KilForm(forms.ModelForm):
	class Meta:
 		model = killed
 		fields = ['SEX', 'AGE', 'TYPE']
    
'''   
        exclude=['ACC_ID','TIME_TYPE','ROAD', 'LOCATION','CATEGORY', 'TWW1', 'TWW2', 'SELF_TYPE', 'INJURED', 'INJMALE','INJFEMALE', 'INJBOY',
 'INJGIRL', 'KILLED', 'KILMALE', 'KILFEMALE', 'KILBOY', 'KILGIRL', 'PEDESTRIAN', 'ACCTYPE',
'ACCID_TYPE','VICTIM', 'DUPL', 'PENDING','DAY_NIGHT','YEAR','TIME_SLOT', 'MONTH','FN','ACCAGE','ACCSEX',
'ACCDRUNK', 'routeno', 'case_status','convert_case', 'BRIEF_FACTS' , 'dri_fath', 'dri_sex', 'dri_lic_status','CONFIRM','CONVERT',
'CONVERT_DATE', 'CN_DT', 'CONVERT_FN','BUS_NO', 'BLACK_SPOT', 'BLACK_SPOT_NO', 'FOR_BLK', 'STATUS',
 'F_STATUS','dri_add1','RIDER_HELMET', 'PILLION_HELMET', 'STATE', 'SCANNED', 'HIT_AND_RUN_UPDATE1']
   '''