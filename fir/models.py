# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import Q
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
FLYOVER_UNDERP_CHOICES=(
   ('Ascending Flyover','Ascending Flyover'),('Descending Flyover','Descending Flyover'), 
   ('Ascending Flyover Loop','Ascending Flyover Loop'), ('Descending Flyover Loop','Desscending Flyover Loop') 
)
TIME_KNOWN_CHOICES=(
     ('Y','YES'),('N','NO'),
)

AREA_CHOICES=(
     ('URBAN','URBAN'),('RURAL','RURAL'),
)

SEX_Choices = (
    ('M','Male'),('F','Female'),
)
CONVERT_Choices=(
    ('Y','YES'),('N','NO'),
)
ARRESTED_Choices=(
    ('Y','Yes'),('N','No'),
)

AGE_Choices = (
    ('<10','<10'),('11-18','11-18'),('19-30','19-30'),('31-40','31-40'),('>40','>40'),
)

VIC_TYPE_CHOICES = (
    ('SCL','School Children'),('PPL','Police Person'),('OTH', 'Other'),
)

TIME_TYPE_CHOICES = (
    ('IN FIR','IN FIR'), ('APPROX','APPROX'),
)
CONVERT_STAT_Choices = (
    ('NO INFORMATION','NO INFORMATION'),('PENDING INVESTIGATION','PENDING INVESTIGATION'),('PENDING TRIAL', 'PENDING TRIAL'),
    ('CONVICTED','CONVICTED'),('ACQUITTED','ACQUITTED'),('CANCELLED', 'CANCELLED'),
)

designation_choices = (
     ('', '-----------'),
    ('DCP','DCP'),('ACP','ACP'),('INS', 'INSPECTOR'),
    ('ARC','ACCIDENT RESEARCH CELL'),
)
circle_choices = (
('', '-----------'),
('PGC','PAHAR GANJ CIRCLE'),
('KBC','KAROL BAGH CIRCLE'),
('KMC','KAMLA MARKET CIRCLE'),
('DGC','DARYA GANJ CIRCLE'),
('KPC','KALYAN PURI CIRCLE'),
('VKC','VIVEK VIHAR CIRCLE'),
('MWC','MANDAWALI CIRCLE'),
('GNC','GANDHI NAGAR CIRCLE'),
('KOT','KOTWALI CIRCLE'),
('CLC','CIVIL LINES CIRCLE'),
('SBC','SADAR BAZAR CIRCLE'),
('SMC','SABZI MANDI CIRCLE'),
('PTC','PARLIAMENT STREET CIRCLE'),
('TRC','TUGHLAK ROAD CIRCLE'),
('PTH','PARLIAMENT HOUSE CIRCLE'),
('TMC','TILAK MARG CIRCLE'),
('CHP','CHANAKYA PURI CIRCLE'),
('BKR','BARA KHAMBA ROAD CIRCLE'),
('SHD','SHAHDARA CIRCLE'),
('SLC','KHAZOORI CIRCLE'),
('SPC','SEEMA PURI CIRCLE'),
('MTC','MODEL TOWN CIRCLE'),
('NRL','BURARI CIRCLE'),
('AVC','ASHOK VIHAR CIRCLE'),
('ALP','NARELA CIRCLE'),
('BWC','BAWANA CIRCLE'),
('RHN','ROHINI CIRCLE'),
('MGP','MANGOL PURI CIRCLE'),
('IGI','I.G. AIR PORT CIRCLE'),
('PAP','PALAM AIRPORT CIRCLE'),
('DRP','DELHI RAILWAYS CIRCLE'),
('RKP','R.K. PURAM CIRCLE'),
('DFC','DEFENCE COLONY CIRCLE'),
('DCC','DELHI CANTT CIRCLE'),
('VVC','VASANT VIHAR CIRCLE'),
('SDV','SUKHDEV VIHAR CIRCLE'),
('LNC','LAJPAT NAGAR CIRCLE'),
('HKC','HAUS KHAS CIRCLE'),
('SVC','SARITA VIHAR CIRCLE'),
('KKC','KALKAJI CIRCLE'),
('SGV','SANGAM VIHAR CIRCLE'),
('SKT','SAKET CIRCLE'),
('GKC','GREATER KAILASH CIRCLE'),
('MRC','MEHRAULI CIRCLE'),
('KHC','KAPASHERA CIRCLE'),
('DWC','DWARKA CIRCLE'),
('TNC','TILAK NAGAR CIRCLE'),
('NJC','NAJAF GARH CIRCLE'),
('JPC','JANAK PURI CIRCLE'),
('NLC','NANGLOI CIRCLE'),
('PNC','PATEL NAGAR CIRCLE'),
('MPC','MAYA PURI CIRCLE'),
('PBC','PUNJABI BAGH CIRCLE'),
('RGC','RAJOURI GARDEN CIRCLE'),
)

YES_NO_CHOICES = (
     ('Y','YES'),('N','NO'),
)

OFFEND_CHOICES = (
     ('OFFENDING','Offending'),('VICTIM VEHICLE','Victim Vehicle'),
)

HELMET_STANDARD_CHOICES = (
     ('STANDARD','Standard'),('SUB STANDARD','Sub Standard'),('NOT KNOWN','Not Known'),
)
CAUSE_Choices = (
     ('KNOWN','Known'),('UNKNOWN','Unknown'),
)

class circles(models.Model):
    DISTNAM = models.CharField(max_length=50)
    DIST = models.CharField(max_length=4)
    CIRCLE = models.CharField(max_length=4, primary_key=True)
    CIRCLENAM = models.CharField(max_length=50)
    RANGE = models.CharField(max_length=4)
    RANGENAM = models.CharField(max_length=50)
    def __str__(self):
        return self.CIRCLENAM

    def as_json(self):
        return dict(
            DISTNAM=self.DISTNAM,
            DIST = self.DIST,
            CIRCLE = self.CIRCLE,
            CIRCLENAM=self.CIRCLENAM,
            RANGE=self.RANGE,
            RANGENAM=self.RANGENAM)
            

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default = "0")
    emp_id = models.CharField(max_length=15, default = "0")
    circle = models.CharField(max_length=60, choices = circle_choices)
    district_circle = models.CharField(max_length=30, blank = True)
    range_circle = models.CharField(max_length=30, blank = True)
    designation = models.CharField(max_length=30, choices = designation_choices)
    #max_attempts = models.PositiveIntegerField(blank = True, default='0')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()


class roads(models.Model):
    RNG =  models.CharField(max_length = 5, blank = True)
    DIST = models.CharField(max_length = 5, blank = True)
    CIRCLE = models.ForeignKey(circles)
    ROADNAME = models.CharField(max_length=50)
    ROAD = models.IntegerField()
    PS = models.CharField(max_length=5, blank = True)
    PLACE_OCC = models.CharField(max_length=50, blank = True)
    NEW = models.CharField(max_length=50, primary_key = True)
    PSNAME = models.CharField(max_length=50, blank = True)
    NEW1 = models.CharField(max_length=50, blank = True)
    def __str__(self):
        return self.ROADNAME

class sections(models.Model):
    SECTION = models.IntegerField(primary_key=True)
    SECTIONDTL = models.CharField(max_length = 50)
    ACCTYPE = models.CharField(max_length = 5)
    ACCTYPEN = models.CharField(max_length = 25)
    def __str__(self):
        return self.SECTIONDTL
    def as_json(self):
        return dict(
            SECTION=self.SECTION,
            SECTIONDTL = self.SECTIONDTL,
            ACCTYPE = self.ACCTYPE,
            ACCTYPEN=self.ACCTYPEN)

class policestation(models.Model):
    DISTNAM = models.CharField(max_length = 50)
    DIST = models.CharField(max_length = 20)
    CIRCLE = models.ForeignKey(circles)
    CIRCLENAM = models.CharField(max_length=50)
    RANGE = models.CharField(max_length=4)
    RANGENAM = models.CharField(max_length=50)
    PS = models.CharField(max_length=20)
    PSNAME = models.CharField(max_length = 100)
    CIRCLE_PS= models.CharField(max_length=50, primary_key = True)
    def __str__(self):
        return self.PSNAME

class self_type(models.Model):
    SNO=models.CharField(max_length=20,primary_key=True)
    CODE=models.CharField(max_length=20)
    TYPE=models.CharField(max_length=100)
    def __str__(self):
        return self.TYPE
        
class location(models.Model):
    SNO = models.PositiveIntegerField(primary_key = True)
    TYPE = models.CharField(max_length = 150)
    CATEGORY = models.CharField(max_length = 100)
    def __str__(self):
        return self.TYPE

    def as_json(self):
        return dict(
            TYPE = self.TYPE,
            CATEGORY = self.CATEGORY)


class accid_type(models.Model):
    SNO=models.PositiveIntegerField(primary_key=True)
    TYPE=models.CharField(max_length=200)
    CATEGORY = models.CharField(max_length = 100)
    CODE=models.CharField(max_length=20, blank=True)
    VICTIM=models.CharField(max_length=50)

    def __str__(self):
        return self.TYPE
    def as_json(self):
        return dict(
            SNO = self.SNO,
            VICTIM = self.VICTIM)    

class victim_person_status(models.Model):

    Victim_Person_Status=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Victim_Person_Status             

class victim_person_status1(models.Model):

    Victim_Person_Status1=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Victim_Person_Status1  

class mva_act(models.Model):
          
    MVA_Section=models.CharField(max_length=20,primary_key=True)
    MVA_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.MVA_Name


                                        
class area_type(models.Model):
          
    Atype_Code=models.CharField(max_length=20,primary_key=True)
    Area_Type=models.CharField(max_length = 100)
    def __str__(self):
        return self.Area_Type


class area_type2(models.Model):
          
    SAtype_Code=models.CharField(max_length=20,primary_key=True)
    SArea_Type=models.CharField(max_length = 100)
    def __str__(self):
        return self.SArea_Type

class area_type2_oth(models.Model):
          
    SOAtype_Code=models.CharField(max_length=20,primary_key=True)
    SOArea_Type=models.CharField(max_length = 100)
    def __str__(self):
        return self.SAOrea_Type


class road_level(models.Model):          
    RL_Code=models.CharField(max_length=20,primary_key=True)
    RL_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.RL_Name


class ground_level(models.Model):
          
    RL_Code=models.CharField(max_length=20)
    RL_Name=models.CharField(max_length = 100)
    GL_Code=models.CharField(max_length=20,primary_key=True)
    GL_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.GL_Code

class junction_control(models.Model):
          
    GL_Code=models.CharField(max_length=20)
    GL_Name=models.CharField(max_length = 100)
    JCTRL_Code=models.CharField(max_length=20)
    JCTRL_Name=models.CharField(max_length = 100)
    GL_JCTRL_Code=models.CharField(max_length=40,primary_key=True)
    def __str__(self):
        return self.GL_JCTRL_Code


class road_type(models.Model):
          
    RT_Code=models.CharField(max_length=20,primary_key=True)
    RT_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.RT_Name


class road_type1(models.Model):
          
    SRT_Code=models.CharField(max_length=20,primary_key=True)
    SRT_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.SRT_Name


class seperation(models.Model):
          
    S_Code=models.CharField(max_length=20,primary_key=True)
    S_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.S_Name


class road_character(models.Model):
          
    RC_Code=models.CharField(max_length=20,primary_key=True)
    RC_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.RC_Name

class surface_type(models.Model):
          
    SFT_Code=models.CharField(max_length=20,primary_key=True)
    SFT_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.SFT_Name


class surface_condition(models.Model):
          
    SC_Code=models.CharField(max_length=20,primary_key=True)
    SC_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.SC_Name

class road_condition(models.Model):
          
    RCN_Code=models.CharField(max_length=20,primary_key=True)
    RCN_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.RCN_Name
   

class study_parameter(models.Model):
          
    SPM_Code=models.CharField(max_length=20,primary_key=True)
    SPM_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.SPM_Name
    
class vehicle_loaded_condition(models.Model):
          
    VLC_Code=models.CharField(max_length=20,primary_key=True)
    VLC_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.VLC_Name
    

class edu_qual(models.Model):
          
    EDQF_Code=models.CharField(max_length=20,primary_key=True)
    EDQF_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.EDQF_Name
    

class work_status(models.Model):
          
    WS_Code=models.CharField(max_length=20,primary_key=True)
    WS_Name=models.CharField(max_length = 100)
    def __str__(self):
        return self.WS_Name
   

class driver_fault(models.Model):
          
    DF_Code=models.CharField(max_length=20,primary_key=True)
    DF_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.DF_Details
    

class veh_mech_fault(models.Model):
          
    VMF_Code=models.CharField(max_length=20,primary_key=True)
    VMF_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.VMF_Details
   

class road_env_fault(models.Model):
          
    REF_Code=models.CharField(max_length=20,primary_key=True)
    REF_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.REF_Details
  


class road_engg_fault(models.Model):
          
    RENF_Code=models.CharField(max_length=20,primary_key=True)
    RENF_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.RENF_Details
 

class victim_fault(models.Model):
          
    VF_Code=models.CharField(max_length=20,primary_key=True)
    VF_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.VF_Details
  
class weather_cond(models.Model):
          
    WC_Code=models.CharField(max_length=20,primary_key=True)
    WC_Details=models.CharField(max_length = 100)
    def __str__(self):
        return self.WC_Details
    
 
class remedies(models.Model):
          
    Rem_Code=models.CharField(max_length=20,primary_key=True)
    Rem_Description=models.CharField(max_length = 100)
    def __str__(self):
        return self.Rem_Description


 
class vehtype1(models.Model):
    VEHTYPE = models.CharField(max_length=20, primary_key= True)
    VEHDETL = models.CharField(max_length=20)
    VEHDTL = models.CharField(max_length=40)
    SIMPLE = models.PositiveIntegerField(default = 0)
    NONINJ = models.PositiveIntegerField(default = 0)
    FATAL = models.PositiveIntegerField(default = 0)
    PERINJ = models.PositiveIntegerField(default = 0)
    PERKIL = models.PositiveIntegerField(default = 0)
    PEDESTRIAN= models.PositiveIntegerField(default = 0)
    CARI= models.PositiveIntegerField(default = 0)
    CARK= models.PositiveIntegerField(default = 0)
    DTCI= models.PositiveIntegerField(default = 0)
    DTCK= models.PositiveIntegerField(default = 0)
    BLBI= models.PositiveIntegerField(default = 0)
    BLBK= models.PositiveIntegerField(default = 0)
    BUSI= models.PositiveIntegerField(default = 0)
    BUSK= models.PositiveIntegerField(default = 0)
    OSBI= models.PositiveIntegerField(default = 0)
    OSBK= models.PositiveIntegerField(default = 0)
    MBSI= models.PositiveIntegerField(default = 0)
    MBSK= models.PositiveIntegerField(default = 0)
    TAXI= models.PositiveIntegerField(default = 0)
    TAXK= models.PositiveIntegerField(default = 0)
    TSRI= models.PositiveIntegerField(default = 0)
    TSRK= models.PositiveIntegerField(default = 0)
    TWWI= models.PositiveIntegerField(default = 0)
    TWWK= models.PositiveIntegerField(default = 0)
    MILI= models.PositiveIntegerField(default = 0)
    MILK= models.PositiveIntegerField(default = 0)
    DLVI= models.PositiveIntegerField(default = 0)
    DLVK= models.PositiveIntegerField(default = 0)
    TRCI= models.PositiveIntegerField(default = 0)
    TRCK= models.PositiveIntegerField(default = 0)
    POVI= models.PositiveIntegerField(default = 0)
    POVK= models.PositiveIntegerField(default = 0)
    AMBI= models.PositiveIntegerField(default = 0)
    AMBK= models.PositiveIntegerField(default = 0)
    STRI= models.PositiveIntegerField(default = 0)
    STRK= models.PositiveIntegerField(default = 0)
    TMPI= models.PositiveIntegerField(default = 0)
    TMPK= models.PositiveIntegerField(default = 0)
    MATI= models.PositiveIntegerField(default = 0)
    MATK= models.PositiveIntegerField(default = 0)
    TNKI= models.PositiveIntegerField(default = 0)
    TNKK= models.PositiveIntegerField(default = 0)
    UNKI= models.PositiveIntegerField(default = 0)
    UNKK= models.PositiveIntegerField(default = 0)
    CYCI= models.PositiveIntegerField(default = 0)
    CYCK= models.PositiveIntegerField(default = 0)
    TNGI= models.PositiveIntegerField(default = 0)
    TNGK= models.PositiveIntegerField(default = 0)
    CYRI= models.PositiveIntegerField(default = 0)
    CYRK= models.PositiveIntegerField(default = 0)
    HDCI= models.PositiveIntegerField(default = 0)
    HDCK= models.PositiveIntegerField(default = 0)
    BULI= models.PositiveIntegerField(default = 0)
    BULK= models.PositiveIntegerField(default = 0)
    ANII= models.PositiveIntegerField(default = 0)
    ANIK= models.PositiveIntegerField(default = 0)
    CRNI= models.PositiveIntegerField(default = 0)
    CRNK= models.PositiveIntegerField(default = 0)
    UDTI= models.PositiveIntegerField(default = 0)
    UDTK= models.PositiveIntegerField(default = 0)
    PEDI= models.PositiveIntegerField(default = 0)
    PEDK= models.PositiveIntegerField(default = 0)
    HTVI= models.PositiveIntegerField(default = 0)
    HTVK= models.PositiveIntegerField(default = 0)
    SLFI= models.PositiveIntegerField(default = 0)
    SLFK= models.PositiveIntegerField(default = 0)
    ELTI= models.PositiveIntegerField(default = 0)
    ELTK= models.PositiveIntegerField(default = 0)
    WLLI= models.PositiveIntegerField(default = 0)
    WLLK= models.PositiveIntegerField(default = 0)
    PASI= models.PositiveIntegerField(default = 0)
    PASK= models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.VEHDETL

class vehtype2(models.Model):
    VEHTYPE=models.CharField(max_length=30, primary_key= True)
    VEHDETL=models.CharField(max_length=20)
    VEHDTL = models.CharField(max_length=40)
    SIMPLE= models.PositiveIntegerField(default = 0)
    NONINJ= models.PositiveIntegerField(default = 0)
    FATAL= models.PositiveIntegerField(default = 0)
    PERINJ= models.PositiveIntegerField(default = 0)
    PERKIL= models.PositiveIntegerField(default = 0)
    PEDESTRIAN= models.PositiveIntegerField(default = 0)
    CARI= models.PositiveIntegerField(default = 0)
    CARK= models.PositiveIntegerField(default = 0)
    DTCI= models.PositiveIntegerField(default = 0)
    DTCK= models.PositiveIntegerField(default = 0)
    BLBI= models.PositiveIntegerField(default = 0)
    BLBK= models.PositiveIntegerField(default = 0)
    BUSI= models.PositiveIntegerField(default = 0)
    BUSK= models.PositiveIntegerField(default = 0)
    OSBI= models.PositiveIntegerField(default = 0)
    OSBK= models.PositiveIntegerField(default = 0)
    MBSI= models.PositiveIntegerField(default = 0)
    MBSK= models.PositiveIntegerField(default = 0)
    TAXI= models.PositiveIntegerField(default = 0)
    TAXK= models.PositiveIntegerField(default = 0)
    TSRI= models.PositiveIntegerField(default = 0)
    TSRK= models.PositiveIntegerField(default = 0)
    TWWI= models.PositiveIntegerField(default = 0)
    TWWK= models.PositiveIntegerField(default = 0)
    MILI= models.PositiveIntegerField(default = 0)
    MILK= models.PositiveIntegerField(default = 0)
    DLVI= models.PositiveIntegerField(default = 0)
    DLVK= models.PositiveIntegerField(default = 0)
    TRCI= models.PositiveIntegerField(default = 0)
    TRCK= models.PositiveIntegerField(default = 0)
    POVI= models.PositiveIntegerField(default = 0)
    POVK= models.PositiveIntegerField(default = 0)
    AMBI= models.PositiveIntegerField(default = 0)
    AMBK= models.PositiveIntegerField(default = 0)
    STRI= models.PositiveIntegerField(default = 0)
    STRK= models.PositiveIntegerField(default = 0)
    TMPI= models.PositiveIntegerField(default = 0)
    TMPK= models.PositiveIntegerField(default = 0)
    MATI= models.PositiveIntegerField(default = 0)
    MATK= models.PositiveIntegerField(default = 0)
    TNKI= models.PositiveIntegerField(default = 0)
    TNKK= models.PositiveIntegerField(default = 0)
    UNKI= models.PositiveIntegerField(default = 0)
    UNKK= models.PositiveIntegerField(default = 0)
    CYCI= models.PositiveIntegerField(default = 0)
    CYCK= models.PositiveIntegerField(default = 0) 
    TNGI= models.PositiveIntegerField(default = 0)
    TNGK= models.PositiveIntegerField(default = 0)
    CYRI= models.PositiveIntegerField(default = 0)
    CYRK= models.PositiveIntegerField(default = 0)
    HDCI= models.PositiveIntegerField(default = 0)
    HDCK= models.PositiveIntegerField(default = 0)
    BULI= models.PositiveIntegerField(default = 0)
    BULK= models.PositiveIntegerField(default = 0)
    ANII= models.PositiveIntegerField(default = 0)
    ANIK= models.PositiveIntegerField(default = 0)
    CRNI= models.PositiveIntegerField(default = 0)
    CRNK= models.PositiveIntegerField(default = 0)
    UDTI= models.PositiveIntegerField(default = 0)
    UDTK= models.PositiveIntegerField(default = 0)
    PEDI= models.PositiveIntegerField(default = 0)
    PEDK= models.PositiveIntegerField(default = 0)
    HTVI= models.PositiveIntegerField(default = 0)
    HTVK= models.PositiveIntegerField(default = 0)
    SLFI= models.PositiveIntegerField(default = 0)
    SLFK= models.PositiveIntegerField(default = 0)
    ELTI= models.PositiveIntegerField(default = 0)
    ELTK= models.PositiveIntegerField(default = 0)
    WLLI= models.PositiveIntegerField(default = 0)
    WLLK= models.PositiveIntegerField(default = 0)
    PASI= models.PositiveIntegerField(default = 0)
    PASK= models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.VEHDETL
          

class details(models.Model):

    ACC_ID = models.CharField(max_length=15, primary_key=True)
    RNG = models.CharField(max_length=5)

    CIRCLE = models.ForeignKey(circles)

    DIST =  models.CharField(max_length=5)
    PS = ChainedForeignKey(policestation,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True)

    FIRNO = models.PositiveIntegerField( validators=[MaxValueValidator(9999), MinValueValidator(1)])
    FIR_DATE = models.DateField('FIR DATE')
    DATE_OCC = models.DateField('DATE_OCC')
    TIME_OCC = models.CharField(max_length=4,default='',blank=True)
    TIME_KNOWN =models.CharField(choices=TIME_KNOWN_CHOICES, max_length = 30)
    SECTION = models.ForeignKey(sections)
    MVA_NAME =models.ForeignKey(mva_act,default='',blank=True)
    FIR_PHOTO = models.FileField(upload_to='documents/',blank=True,default='')
    ACC_PHOTO = models.FileField(upload_to='documents/',blank=True,default='')




    PLACE_OCC = models.CharField(max_length=140,blank=True, default='')
    AREA =models.CharField(choices=AREA_CHOICES, max_length = 30)
    LOCATION = models.ForeignKey(location, blank=True,default = 0)
    ACC_SKETCH_PHOTO = models.FileField(upload_to='documents/',blank=True,default='')
    AREA_TYPE = models.ForeignKey(area_type,default='',blank=True)
    AREA_TYPE_OTHER = models.CharField(max_length=140,blank=True, default='')
    SAREA_TYPE=models.ForeignKey(area_type2,default='',blank=True)
    SOAREA_TYPE=models.ForeignKey(area_type2_oth,default='',blank=True)


    ROAD = ChainedForeignKey(
        roads,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True)

    ROADNAME = models.CharField(max_length=150)
    MINORROADNAME = models.CharField(max_length=150)

    ROAD_LEVEL = models.ForeignKey(road_level,default='',blank=True)
    GROUND_LEVEL=models.ForeignKey(ground_level,default='',blank=True)
    FLYOVER_UNDERP =models.CharField(choices=FLYOVER_UNDERP_CHOICES, max_length = 30)

    JUNCTION_CONTROL=models.ForeignKey(junction_control,default='',blank=True)
    ROAD_TYPE=models.ForeignKey(road_type,default='',blank=True)
    ROAD_TYPE1=models.ForeignKey(road_type1,default='',blank=True)
    SEPERATION = models.ForeignKey(seperation,default='',blank=True)
    ROAD_CHARACTER = models.ForeignKey(road_character,default='',blank=True)
    ROAD_CHARACTER_REMARKS= models.CharField(max_length=15,blank=True, default=0)
    SURFACE_TYPE = models.ForeignKey(surface_type,default='',blank=True)
    SURFACE_CONDITION = models.ForeignKey(surface_condition,default='',blank=True)
    SURFACE_CONDITION_REMARKS = models.CharField(max_length=15,blank=True, default=0)
    ROAD_CONDITION = models.ForeignKey(road_condition,default='',blank=True)
    ROAD_CONDITION_REMARKS = models.CharField(max_length=15,blank=True, default=0)
    
    CATEGORY = models.CharField(max_length=140,blank=True, default =0)
    

    

    
    SELF_TYPE = models.ForeignKey(self_type, default=0,blank=True)

    INJURED = models.PositiveIntegerField(default = 0, blank=True)
    INJMALE = models.PositiveIntegerField(default = 0, blank=True)
    INJFEMALE = models.PositiveIntegerField(default = 0, blank=True)
    INJBOY = models.PositiveIntegerField(default = 0, blank=True)
    INJGIRL = models.PositiveIntegerField(default = 0,blank=True)
    KILLED = models.PositiveIntegerField(default = 0,blank=True)
    KILMALE = models.PositiveIntegerField(default = 0,blank=True)
    KILFEMALE = models.PositiveIntegerField(default = 0,blank=True)
    KILBOY = models.PositiveIntegerField(default = 0,blank=True)
    KILGIRL = models.PositiveIntegerField(default = 0,blank=True)
    PEDESTRIAN = models.PositiveIntegerField(default = 0,blank=True)
    
    ACCTYPE = models.CharField(max_length=20,blank=True)

    ACCID_TYPE = models.ForeignKey(accid_type, default = 0)

    VICTIM = models.CharField(max_length=100,blank = True, default = 0)

    DUPL = models.CharField(max_length=15, blank=True, default = 0)
    PENDING = models.CharField(max_length=15,blank=True,default = 0)

    DAY_NIGHT = models.CharField(max_length=15)
    YEAR = models.PositiveIntegerField()
    TIME_SLOT = models.CharField(max_length=15)
    MONTH = models.CharField(max_length=15)
    FN = models.CharField(max_length=15)

    ACCAGE = models.CharField(max_length=15, blank=True,default=0)
    ACCSEX = models.CharField(max_length=15, choices = SEX_Choices, blank=True, default = '')

    Intersection = models.CharField(max_length=150, blank=True, default = '')
    case_status = models.CharField(max_length=15, blank=True, choices = CONVERT_STAT_Choices, default = '')
    convert_case = models.CharField(max_length=15,blank=True, default = '')
    
    BRIEF_FACTS = models.CharField(max_length=500,blank=True, default = '')
    

    
    dri_lic_status = models.CharField(max_length=15,blank=True, default = '')
    
    REMARK = models.CharField(max_length=500, default = '', blank=True)
    CONFIRM = models.CharField(max_length=15, default = '' ,blank=True)
    LONGITUDE = models.CharField(max_length=15, blank =  True, default = '')
    LATITUDE = models.CharField(max_length=15, blank = True, default = '')
    
    #CAUSE ANALYSIS
    CAUSE = models.CharField(max_length=15,choices=CAUSE_Choices)
    DRIVER_FAULT = models.ForeignKey(driver_fault,default='',blank=True)
    OTHER_DRIVER_FAULT = models.CharField(max_length=50,blank=True, default = '')
    OVER_SPEED_FAULT = models.CharField(max_length=15,choices=YES_NO_CHOICES)
    VEH_MECH_FAULT = models.ForeignKey(veh_mech_fault,default='',blank=True)
    OTHER_VEC_MEH_FAULT = models.CharField(max_length=50,blank=True, default = '')
    ROAD_ENV_FAULT = models.ForeignKey(road_env_fault,default='',blank=True)
    OTHER_ROAD_ENV_FAULT = models.CharField(max_length=50,blank=True, default = '')
    ROAD_ENGG_FAULT = models.ForeignKey(road_engg_fault,default='',blank=True)
    OTHER_ROAD_ENGG_FAULT = models.CharField(max_length=50,blank=True, default = '')
    VICTIM_FAULT = models.ForeignKey(victim_fault,default='',blank=True)
    OTHER_VICTIM_FAULT = models.CharField(max_length=50,blank=True, default = '')
    WEATHER_COND = models.ForeignKey(weather_cond,default='',blank=True)
    OTHER_WEATHER_COND_FAULT = models.CharField(max_length=50,blank=True, default = '')
    OTHER_FAULT = models.CharField(max_length=50,blank=True, default = '')
    #END OF CAUSE ANALYSIS

    CONVERT = models.CharField(max_length=15,choices=CONVERT_Choices,default = 'N')
    CONVERT_DATE = models.DateField(null=True)
    CN_DT = models.CharField(max_length=1000,blank=True, default = 0)
    
    CONVERT_FN = models.CharField(max_length=150,blank=True, default = 0)
    BUS_NO = models.CharField(max_length=15, default = 0, blank=True)
    BLACK_SPOT = models.CharField(max_length=15, default = '', blank=True)
    BLACK_SPOT_NO = models.CharField(max_length=15,default=0,blank=True)
    FOR_BLK = models.CharField(max_length=15,default='',blank=True)
    STATUS = models.CharField(max_length=15,default='',blank=True)
    F_STATUS = models.CharField(max_length=15,default='',blank=True)
    dri_add1 = models.CharField(max_length=15,default='',blank=True)
    RIDER_HELMET = models.CharField(max_length=15,default='',blank=True)
    PILLION_HELMET = models.CharField(max_length=15,default='',blank=True)
    STATE = models.CharField(max_length=15,default='',blank=True)
    SCANNED = models.CharField(max_length=15,default='',blank=True)
    HIT_AND_RUN_UPDATE1 = models.CharField(max_length=15,default='',blank=True)

    VICTIM_PERSON_STATUS = models.ForeignKey(victim_person_status,default='',blank=True)
    VICTIM_PERSON_STATUS1 = models.ForeignKey(victim_person_status1,default='',blank=True)
    REMEDIES = models.ForeignKey(remedies,default='',blank=True)

class offender(models.Model):
    #offending vehicle
    VEHTYPE1 = models.ForeignKey(vehtype1)
    SUBVEHICLE_TYPE1 = models.CharField(max_length=15,blank=True, default=0)
    routeno1 = models.CharField(max_length=15, default = 0, blank=True)
    rcno1 = models.CharField(max_length=15, default = 0, blank=True)
    VEHICLE_LOADED_CONDITION1 = models.ForeignKey(vehicle_loaded_condition,default='',blank=True)
    STUDY_PARAMETER1 = models.ForeignKey(study_parameter,default='',blank=True)
    dri_name = models.CharField(max_length=150,blank=True, default = '')
    dri_rel_name = models.CharField(max_length=150,blank=True, default = '')
    dri_sex = models.CharField(max_length=15, choices = SEX_Choices,blank=True,default='')
    dri_age = models.PositiveIntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)],blank=True, default= 0)
    dri_add = models.CharField(max_length=150,blank=True, default = '')
    EDU_QUAL = models.ForeignKey(edu_qual,default='',blank=True)
    OTHER_EDU_QUAL = models.CharField(max_length=50, blank=True,default='')
    WORK_STATUS = models.ForeignKey(work_status,default='',blank=True)
    OTHER_WORK_STATUS = models.CharField(max_length=50, blank=True,default='')
    DRI_DRUNK = models.BooleanField()
    dri_lic_no = models.CharField(max_length=150,blank=True, default = '')
    dri_lic_from = models.CharField(max_length=150,blank=True, default = '')
    dri_lic_date_issu = models.DateField(null=True)
    dri_lic_date_upto = models.DateField(null=True)
    RNOV1A = models.CharField(max_length=4, default=0, blank=True)
    RNOV1B = models.CharField(max_length=4, default=0, blank=True)
    #offending vehicle end
    dri_lic_status = models.CharField(max_length=15,blank=True, default = '')

class victim_vehicle(models.Model):
    #victim vehicle 
    VEHTYPE2 = models.ForeignKey(vehtype2)
    SUBVEHICLE_TYPE2 = models.CharField(max_length=15, default=0, blank=True)
    routeno2 = models.CharField(max_length=15, default = 0, blank=True)
    rgno2 = models.CharField(max_length=15, default = 0, blank=True)
    VEHICLE_LOADED_CONDITION2 = models.ForeignKey(vehicle_loaded_condition,default='',blank=True)
    STUDY_PARAMETER2 = models.ForeignKey(study_parameter,default='',blank=True)
    #victim vehicle end

class victim(models.Model):
    VIC_TYPE = models.CharField(max_length=15, choices = VIC_TYPE_CHOICES)
    VICSEX = models.CharField(max_length=15, choices = SEX_Choices)
    VICAGE = models.CharField(max_length = 15, choices = AGE_Choices)
    VICTYPE = models.CharField(max_length = 15, choices = VIC_TYPE_CHOICES)
    VICTYPE1 = models.ForeignKey(victim_person_status1)
    VIC_IN_VEH = models.CharField(max_length = 5, choices = YES_NO_CHOICES)
    OFFEND = models.CharField(max_length = 15, choices = OFFEND_CHOICES)
    #VEH_INFO = models.CharField(max_length = 5, choices = OFFEND_CHOICES)
    VIC_SEAT_BELT = models.CharField(max_length = 5, choices = YES_NO_CHOICES)
    VIC_HELMET = models.CharField(max_length = 5, choices = YES_NO_CHOICES)
    HELMET_STANDARD = models.CharField(max_length = 15, choices = HELMET_STANDARD_CHOICES)
    VIC_EDU_QUAL = models.ForeignKey(edu_qual,default='',blank=True)
    VIC_OTHER_EDU_QUAL = models.CharField(max_length=50, blank=True,default='')
    VIC_WORK_STATUS = models.ForeignKey(work_status,default='',blank=True)
    VIC_OTHER_WORK_STATUS = models.CharField(max_length=50, blank=True,default='')
    VIC_DRI_DRUNK = models.BooleanField()
    ACCID_ID = models.ForeignKey(details)

class collision(models.Model):

    VIC_TYPE = models.CharField(max_length=15)
    COL_TYPE = models.CharField(max_length = 15)
    ACCID_ID = models.ForeignKey(details)


class injured(models.Model):
    PS = models.CharField(max_length=5)
    FIRNO = models.IntegerField()
    YEAR = models.PositiveIntegerField()
    INJSEX = models.CharField(max_length=15, choices = SEX_Choices)
    INJAGE = models.CharField(max_length = 15, choices = AGE_Choices)
    INJTYPE = models.CharField(max_length = 5, choices = VIC_TYPE_CHOICES)
    ACCID_ID = models.ForeignKey(details)

class killed(models.Model):
    PS = models.CharField(max_length=5)
    FIRNO = models.IntegerField()
    YEAR = models.PositiveIntegerField()
    SEX = models.CharField(max_length = 15, choices = SEX_Choices)
    AGE = models.CharField(max_length = 15, choices = AGE_Choices)
    TYPE = models.CharField(max_length = 20, choices = VIC_TYPE_CHOICES)
    ACCID_ID = models.ForeignKey(details)

