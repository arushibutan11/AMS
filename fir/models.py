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
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

# Create your models here.
VEHTYPE_CHOICES=(
('AMBULANCE','AMBULANCE'),
('ANIMAL','ANIMAL'),
('BULLOCK CARTS','BULLOCK CARTS'),
('BUS BLUE LINE','BUS BLUE LINE'),
('BUS DTC','BUS DTC'),
('BUS MINI/RTV','BUS MINI/RTV'),
('BUS OTHER','BUS OTHER'),
('BUS OTHER STATE','BUS OTHER STATE'),
('BUS SCHOOL','BUS SCHOOL'),
('BUS UNDER DTC','BUS UNDER DTC'),
('CALL CENTER CAB','CALL CENTER CAB'),
('CAR PVT','CAR PVT'),
('CLUSTER BUS','CLUSTER BUS'),
('CRANE','CRANE'),
('CYCLE RICKSHOW','CYCLE RICKSHOW'),
('CYCLIST','CYCLIST'),
('DELIVERY VAN','DELIVERY VAN'),
('E RICKSHAW','E RICKSHAW'),
('ELECTRIC BIKE','ELECTRIC BIKE'),
('GRAMIN SEWA','GRAMIN SEWA'),
('HAND CARTS','HAND CARTS'),
('HTV/GOODS','HTV/GOODS'),
('MATADOR','MATADOR'),
('MILITARY VEH.','MILITARY VEH.'),
('POLICE VEHICLE','POLICE VEHICLE'),
('SCOOTRIST/MC','SCOOTRIST/MC'),
('STEEM ROLLER','STEEM ROLLER'),
('TANKER','TANKER'),
('TAXI','TAXI'),
('TEMPO','TEMPO'),
('TONGA/REHRA','TONGA/REHRA'),
('TRACTOR','TRACTOR'),
('TRAILER/CONTANR','TRAILER/CONTANR'),
('TSR','TSR'),
('UN-KNOWN VEH.','UN-KNOWN VEH.'),)

VICTIM_CHOICES=(
('SELF','SELF'),
('SELF/ANIMAL','SELF/ANIMAL'),
('PASSENGER','PASSENGER'),
('PEDESTRIAN','PEDESTRIAN'),
('VEHICLES','VEHICLES'),
('VEHICLES/PED','VEHICLES/PED'),
)

SUBVEHICLE_TYPE_CHOICE=(
    ('Scooter','Scooter'),
    ('Scooty','Scooty'),
    ('Motor bike','Motor bike'),
    ('N/A','N/A'),

    )
FLYOVER_CHOICES=(
   ('Ascending Flyover','Ascending Flyover'),('Descending Flyover','Descending Flyover'),
   ('Ascending Flyover Loop','Ascending Flyover Loop'), ('Descending Flyover Loop','Descending Flyover Loop')
)
UNDERP_CHOICES=(
   ('Ascending Underpass','Ascending Underpass'),('Descending Underpass','Descending Underpass'),
)
ROAD_LEVEL_Choices=(
   ('FLYO','Flyover'),('UNPA','Underpass'),('GRL','Ground Level'),
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
GROUND_LEVEL_Choices=(
    ('JUN','Junction'),('ROA','Round About'),('ROS','Road Stretch'),('TPT','T Point'),('CUT','Cut'),

)
JUNC_CTRL_Choices=(
    ('BLK','Blinker'),('PM','Police/Manual'),('SBM','Signal on Blinking Mode'),('SNW','Signal Not Working'),('SW','Signal Working'),('UNC','Signal Uncontrolled'),

)
AGE_Choices = (
    ('<10','<10'),('11-18','11-18'),('19-30','19-30'),('31-40','31-40'),('>40','>40'),
)
INJKIL_CHOICES = (
    ('INJURED','Injured'),('KILLED','Killed'),
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
     ('', 'Designation'),
    ('DCP','DCP'),('ACP','ACP'),('INS', 'INSPECTOR'),
    ('ARC','ACCIDENT RESEARCH CELL'),
)
RELATION_CHOICES = (
    ('S/O','S/O'),('D/O','D/O'),('W/O', 'W/O'),
)
circle_choices = (
('', 'Circle'),
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
DRUNK_CHOICES = (
     ('Y','YES'),('N','NO'),('UNKNOWN','UNKNOWN')
)


OFFEND_CHOICES = (
     ('OFFENDING VEHICLE','Offending Vehicle'),('VICTIM VEHICLE','Victim Vehicle'),
)
ILLUMINATION_CHOICES =  (
     ('WORKING','Working'),('NOT WORKING','Not Working'),
)
ROAD_MARKING_CHOICES =  (
     ('YES','Yes'),('NO','No'),('FADED','Faded'),
)
ROAD_SIGN_CHOICES =  (
     ('SUFFICIENT','Sufficient'),('NOT SUFFICIENT','Not Sufficient'),
)
HELMET_STANDARD_CHOICES = (
     ('STANDARD','Standard'),('SUB STANDARD','Sub Standard'),('NOT KNOWN','Not Known'),
)
CAUSE_Choices = (
     ('KNOWN','Known'),('UNKNOWN','Unknown'),
)
ROAD_TYPE1_Choices = (
     ('ONE WAY','One Way'),('TWO WAY','Two Way'),
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
    designation = models.CharField(max_length=30, choices = designation_choices)
    circle = models.CharField(max_length=60, choices = circle_choices,blank = True,default='')
    district_circle = models.CharField(max_length=30, blank = True)
    range_circle = models.CharField(max_length=30, blank = True)
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
        return self.TYPE + ' (' + self.VICTIM +')'
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
        return self.SOArea_Type


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
    #FIR DETAILS
    ACC_ID = models.CharField(max_length=15, primary_key=True,  verbose_name = 'Accident ID')
    CIRCLE = models.ForeignKey(circles, verbose_name = 'Circle')
    DIST =  models.CharField(max_length=5, verbose_name = 'District')
    RNG = models.CharField(max_length=5, verbose_name = 'Range')
    PS = ChainedForeignKey(policestation,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name = 'Police Station')

    FIRNO = models.PositiveIntegerField( verbose_name = 'FIR No.', validators=[MaxValueValidator(9999), MinValueValidator(1)])
    FIR_DATE = models.DateField('FIR Date')
    DATE_OCC = models.DateField('Accident Date')
    TIME_KNOWN =models.CharField(choices=TIME_KNOWN_CHOICES, max_length = 30, verbose_name = 'Time Known')
    TIME_OCC = models.CharField(max_length=4,default='',blank=True, verbose_name = 'Time')
    OF_SECTION = models.ForeignKey(sections, verbose_name = 'Section')
    MVA_NAME =models.ForeignKey(mva_act,blank=True, null=True,verbose_name = 'MVA Act')
    ACC_PHOTO = models.FileField(upload_to='documents/',blank=True,null=True,default='', verbose_name = 'Picture of Accident ')
    FIR_PHOTO = models.FileField(upload_to='documents/',blank=True,null=True,default='', verbose_name = 'Picture of FIR ')
    #END OF FIR DETAILS



    #LOCATION
    PLACE_OCC = models.CharField(max_length=140,blank=True, default='', verbose_name = 'Place of Occurence')
    AREA =models.CharField(choices=AREA_CHOICES, max_length = 30, verbose_name = 'Area')
    map_loc = LocationField(based_fields=['PLACE_OCC'], zoom=7, verbose_name = 'Lat/Long', default=Point(77.1025, 28.7041))
    ACC_SKETCH_PHOTO = models.FileField(upload_to='documents/',blank=True,null=True,default='', verbose_name = 'Sketch of Accident')
    AREA_TYPE = models.ForeignKey(area_type, verbose_name = 'Area Type')
    AREA_TYPE_OTHER = models.CharField(max_length=50,blank=True, default='', null =  True, verbose_name = 'Other Area Type')
    '''AREA_TYPE2=models.ForeignKey(area_type2, verbose_name = 'Area Type 2')
    AREA_TYPE2_OTHER=models.ForeignKey(area_type2_oth,default='',blank=True, null =  True, verbose_name = 'Other Area Type 2')'''
    AREA_TYPE2 = models.ForeignKey(location, blank=True,verbose_name = 'Location', default=11)
    ROAD = ChainedForeignKey(
        roads,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name = 'Road')

    ROADNAME = models.CharField(max_length=150, verbose_name = 'Road Name')
    MINORROADNAME = models.CharField(max_length=150, default='',blank=True, verbose_name = 'Minor Road')
    ROAD_LEVEL = models.CharField(choices=ROAD_LEVEL_Choices,blank=True, max_length = 30, verbose_name = 'Road Level')
    GROUND_LEVEL=models.CharField(choices=GROUND_LEVEL_Choices,blank=True, max_length = 30, verbose_name = 'Ground Level')
    FLYOVER =models.CharField(choices=FLYOVER_CHOICES, max_length = 30,blank=True, verbose_name = 'Flyover')
    UNDERPASS =models.CharField(choices=UNDERP_CHOICES, max_length = 30,blank=True, verbose_name = 'Underpass')
    JUNCTION_CONTROL=models.CharField(choices=JUNC_CTRL_Choices,blank=True, max_length = 30, verbose_name = 'Junction')
    ROAD_TYPE=models.ForeignKey(road_type, verbose_name = 'Road Type')
    ROAD_TYPE1=models.CharField(choices=ROAD_TYPE1_Choices,blank=True, max_length = 30, verbose_name = 'Road Type 1')
    SEPERATION = models.ForeignKey(seperation, verbose_name = 'Separation')
    ROAD_CHARACTER = models.ForeignKey(road_character, verbose_name = 'Character of Road')
    ROAD_CHARACTER_REMARKS= models.CharField(max_length=50,blank=True, default='', verbose_name = 'Road Character-Remarks')
    SURFACE_TYPE = models.ForeignKey(surface_type, verbose_name = 'Surface Type')
    SURFACE_CONDITION = models.ForeignKey(surface_condition, verbose_name = 'Surface Condition')
    SURFACE_CONDITION_REMARKS = models.CharField(max_length=50,blank=True, default='', verbose_name = 'Surface Condition-Remarks')
    ROAD_CONDITION = models.ForeignKey(road_condition, verbose_name = 'Road Condition')
    ROAD_CONDITION_REMARKS = models.CharField(max_length=50,blank=True, default='', verbose_name = 'Road Condition- Remarks')
    APZ = models.CharField(max_length=50,blank=True, default='', verbose_name = 'Accident Prone Zone')
    APZ_TYPE = models.CharField(max_length=50,blank=True, default='', verbose_name = 'APZ Type')
    ILLUMINATION = models.CharField(max_length=50,blank=True, choices=YES_NO_CHOICES, verbose_name = 'Illumination')
    YES_ILLUMINATION = models.CharField(max_length=50,blank=True, choices=ILLUMINATION_CHOICES, verbose_name = 'Illumination Working')
    ROAD_MARKING = models.CharField(max_length=50,blank=True, choices=ROAD_MARKING_CHOICES, verbose_name = 'Road Markings')
    ROAD_SIGN = models.CharField(max_length=50,blank=True, choices=ROAD_SIGN_CHOICES, verbose_name = 'Road Signs')



    #END OF LOCATION


    #END OF REMARKS
    #DOUBTFUL
    '''SELF_TYPE = models.ForeignKey(self_type, default=0,blank=True)
    CATEGORY = models.CharField(max_length=140,blank=True, default =0)
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

    ACCAGE = models.CharField(max_length=15, blank=True,default=0)
    ACCSEX = models.CharField(max_length=15, choices = SEX_Choices, blank=True, default = '')
    Intersection = models.CharField(max_length=150, blank=True, default = '')
    case_status = models.CharField(max_length=15, blank=True, choices = CONVERT_STAT_Choices, default = '')
    convert_case = models.CharField(max_length=15,blank=True, default = '')
    CONFIRM = models.CharField(max_length=15, default = '' ,blank=True)
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
    HIT_AND_RUN_UPDATE1 = models.CharField(max_length=15,default='',blank=True)'''
    #END OF DOUBTFUL

    MONTH = models.CharField(max_length=15, blank= True)
    FN = models.CharField(max_length=15, blank= True)

class offender(models.Model):
    ACCID_ID = models.ForeignKey(details)
    #offending vehicle
    VEHTYPE1 = models.ForeignKey(vehtype1,verbose_name = 'Type of Vehicle')
    SUBVEHICLE_TYPE1 = models.CharField(max_length=15,blank=True, default='N/A',verbose_name = 'Sub Vehicle Type',choices= SUBVEHICLE_TYPE_CHOICE) #Not clear
    routeno1 = models.CharField(max_length=15, default = 0, blank=True,verbose_name = 'Route No.')
    rcno1 = models.CharField(max_length=15, default = 0, blank=True,verbose_name = 'RC No.')
    VEHICLE_LOADED_CONDITION1 = models.ForeignKey(vehicle_loaded_condition,verbose_name = 'Load of Vehicle')
    STUDY_PARAMETER1 = models.ForeignKey(study_parameter,default='',blank=True,verbose_name = 'Study Parameters',null=True)
    dri_name = models.CharField(max_length=50,blank=True, default = '',verbose_name = 'Name of Driver')
    dri_relation = models.CharField(max_length=15, choices = RELATION_CHOICES, blank=True, default = '',verbose_name = 'Relative of Driver')
    dri_rel_name = models.CharField(max_length=150,blank=True, default = '',verbose_name = 'Name of Relative')
    dri_sex = models.CharField(max_length=15, choices = SEX_Choices,blank=True,default='',verbose_name = 'Gender')
    dri_age = models.PositiveIntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)],blank=True, default= 0,verbose_name = 'Age')
    dri_add = models.CharField(max_length=150,blank=True, default = '',verbose_name = 'Address')
    EDU_QUAL = models.ForeignKey(edu_qual,default='',blank=True,verbose_name = 'Educational Qualifications',null=True)
    OTHER_EDU_QUAL = models.CharField(max_length=50, blank=True,default='',verbose_name = 'Educational Qualifications - Other')
    WORK_STATUS = models.ForeignKey(work_status,default='',blank=True,verbose_name = 'Work Status',null=True)
    OTHER_WORK_STATUS = models.CharField(max_length=50, blank=True,default='',verbose_name = 'Work Status - Other')
    DRI_DRUNK = models.CharField(max_length=50,blank=True, verbose_name = 'Driver Drunk/Not')
    dri_lic = models.CharField(max_length = 5, choices = YES_NO_CHOICES,verbose_name = 'Driver has License?', blank = True)
    dri_lic_no = models.CharField(max_length=150,blank=True, default = '',verbose_name = 'License No.')
    dri_lic_from = models.CharField(max_length=150,blank=True, default = '',verbose_name = 'Driver License From')
    dri_lic_date_issu = models.DateField(null=True,verbose_name = 'License Issue Date')
    dri_lic_date_upto = models.DateField(null=True,verbose_name = 'License Upto Date')

    #offending vehicle end



class victim_vehicle(models.Model):
    ACCID_ID = models.ForeignKey(details)
    #victim vehicle
    VEHTYPE2 = models.ForeignKey(vehtype2,verbose_name = 'Type of Vehicle')
    SUBVEHICLE_TYPE2 = models.CharField(max_length=15, default='N/A', blank=True,verbose_name = 'Sub Vehicle Type',choices= SUBVEHICLE_TYPE_CHOICE)  #Not clear
    routeno2 = models.CharField(max_length=15, default = 0, blank=True,verbose_name = 'Route No.')
    rgno2 = models.CharField(max_length=15, default = 0, blank=True,verbose_name = 'Registration No.')
    VEHICLE_LOADED_CONDITION2 = models.ForeignKey(vehicle_loaded_condition,verbose_name = 'Load of Vehicle')
    STUDY_PARAMETER2 = models.ForeignKey(study_parameter,default='',blank=True,verbose_name = 'Study Parameters',null=True)

    #victim vehicle end

class victim_person(models.Model):
    ACCID_ID = models.ForeignKey(details)
    INJKIL = models.CharField(max_length=15, choices = INJKIL_CHOICES,verbose_name = 'Injured or Killed')
    VICSEX = models.CharField(max_length=15, choices = SEX_Choices,verbose_name = 'Gender')
    VICAGE = models.PositiveIntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)],blank=True, default= 0, verbose_name = 'Age')
    PER_STAT_TYPE = models.CharField(max_length = 15, choices = VIC_TYPE_CHOICES,verbose_name = 'Type of Person')
    PER_STAT_TYPE2 = models.ForeignKey(victim_person_status1,verbose_name = 'Person Status')
    VIC_IN_VEH = models.CharField(max_length = 5, choices = YES_NO_CHOICES,verbose_name = 'Victim inside/outside Vehicle')
    OFFEND = models.CharField(max_length = 20, choices = OFFEND_CHOICES, blank=True,default='',verbose_name = 'Offending/Victim Vehicle')
    VEH_INFO = models.CharField(max_length = 25, blank = True, default='',verbose_name = 'Vehicle Info',choices=VEHTYPE_CHOICES) #NOT CLEAR
    #VEH_INFO = models.ForeignKey(vehtype1,verbose_name = 'Vehicle Info')
    VIC_SEAT_BELT = models.CharField(max_length = 5, choices = YES_NO_CHOICES, blank=True,default='',verbose_name = 'Seatbelt Worn')
    VIC_HELMET = models.CharField(max_length = 5, choices = YES_NO_CHOICES, blank=True,default='',verbose_name = 'Helmet Worn')
    HELMET_STANDARD = models.CharField(max_length = 15, choices = HELMET_STANDARD_CHOICES, blank=True,default='',verbose_name = 'Standard of Helmet')
    VIC_EDU_QUAL = models.ForeignKey(edu_qual,default='',blank=True,verbose_name = 'Educational Qualifications',null=True)
    VIC_OTHER_EDU_QUAL = models.CharField(max_length=50, blank=True,default='',verbose_name = 'Educational Qualifications - Other')
    VIC_WORK_STATUS = models.ForeignKey(work_status,default='',blank=True,verbose_name = 'Work Status',null=True)
    VIC_OTHER_WORK_STATUS = models.CharField(max_length=50, blank=True,default='',verbose_name = 'Work Status - Other')
    VIC_DRI_DRUNK = models.CharField(max_length = 15, choices = DRUNK_CHOICES,verbose_name = 'Drunk/Not')


class collision(models.Model):
    ACCID_ID = models.ForeignKey(details)
    VIC_TYPE = models.CharField(choices = VICTIM_CHOICES, max_length=15,verbose_name = 'Victim Type')
    COL_TYPE = models.ForeignKey(accid_type, verbose_name = 'Type of Collision')
    #CAUSE ANALYSIS

class causes(models.Model):
    ACCID_ID = models.ForeignKey(details)
    CAUSE = models.CharField(max_length=15,choices=CAUSE_Choices, verbose_name = 'Cause')
    DRIVER_FAULT = models.ForeignKey(driver_fault,default='',blank=True, verbose_name = 'Fault of Driver',null =  True)
    OTHER_DRIVER_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Fault of Driver-Other')

    DRUNK_FAULT = models.CharField(max_length=25,blank=True, default = '', verbose_name = 'Case of Drunk Driving')
    OVER_SPEED_FAULT = models.CharField(max_length=15,choices=YES_NO_CHOICES,default='',blank=True, verbose_name = 'Case of Overspeeding')

    VEH_MECH_FAULT = models.ForeignKey(veh_mech_fault,null=True,blank=True, verbose_name = 'Mechanical Fault of Vehicle')
    OTHER_VEC_MEH_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Mechanical Fault -Other')

    ROAD_ENV_FAULT = models.ForeignKey(road_env_fault,null=True,blank=True, verbose_name = 'Fault of Road Environment')
    OTHER_ROAD_ENV_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Road Environment Fault -Other')

    ROAD_ENGG_FAULT = models.ForeignKey(road_engg_fault,null=True,blank=True, verbose_name = 'Fault of Road Engineering')
    OTHER_ROAD_ENGG_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Road Engineering Fault - Other')

    VICTIM_FAULT = models.ForeignKey(victim_fault,null=True,blank=True, verbose_name = 'Fault of Victim')
    OTHER_VICTIM_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Fault of Victim - Other')

    WEATHER_COND = models.ForeignKey(weather_cond,null=True,blank=True, verbose_name = 'Weather Conditions')
    OTHER_WEATHER_COND_FAULT = models.CharField(max_length=50,blank=True, default = '', verbose_name = 'Weather Conditions - Other')

    OTHER_CAUSE = models.CharField(max_length=1000,blank=True, default = '', verbose_name = 'Other Causes')
    #END OF CAUSE ANALYSIS

    #REMARKS
    REMEDIES = models.ForeignKey(remedies, verbose_name = 'Remedies')
    REMARKS = models.CharField(max_length=200,default='',blank=True, verbose_name = 'Remarks')
    OTHER_REMARK = models.CharField(max_length=50, default = '', blank=True, verbose_name = 'Other Remarks')

#REMOVE BUT HOW

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
