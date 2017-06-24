# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import Q
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
SEX_Choices = (
    ('M','Male'),('F','Female'),
)
CONVERT_Choices=(
    ('Y','YES'),('N','NO'),)
ARRESTED_Choices=(
    ('Y','Yes'),('N','No'),)

AGE_Choices = (
    ('<10','<10'),('11-18','11-18'),('19-30','19-30'),('31-40','31-40'),('>40','>40'),
)

INJ_TYPE_CHOICES = (
    ('SCL','School Children'),('PPL','Police Person'),('OTH', 'Other'),
)

TIME_TYPE_CHOICES = (
    ('IN FIR','IN FIR'), ('APPROX.','APPROX.'),
)
CONVERT_STAT_Choices = (
    ('NO INFORMATION','NO INFORMATION'),('PENDING INVESTIGATION','PENDING INVESTIGATION'),('PENDING TRIAL', 'PENDING TRIAL'),
    ('CONVICTED','CONVICTED'),('ACQUITTED','ACQUITTED'),('CANCELLED', 'CANCELLED'),
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

    SECTION = models.ForeignKey(sections)

    TIME_OCC = models.CharField(max_length=4,default='',blank=True)
    TIME_TYPE = models.CharField(max_length=15, choices = TIME_TYPE_CHOICES)
    DATE_OCC = models.DateField('DATE_OCC')
    PLACE_OCC = models.CharField(max_length=140,blank=True, default='')

    ROAD = ChainedForeignKey(
        roads,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True)

    ROADNAME = models.CharField(max_length=150)
    
    LOCATION = models.ForeignKey(location, blank=True,default = 0)
    CATEGORY = models.CharField(max_length=140,blank=True, default =0)
    
    VEHTYPE1 = models.ForeignKey(vehtype1)
    TWW1 = models.CharField(max_length=15,blank=True, default=0)
    RNOV1A = models.CharField(max_length=4, default=0, blank=True)
    RNOV1B = models.CharField(max_length=4, default=0, blank=True)
    
    VEHTYPE2 = models.ForeignKey(vehtype2)
    TWW2 = models.CharField(max_length=15, default=0, blank=True)
    RNOV2A = models.CharField(max_length=4, default=0, blank=True)
    RNOV2B = models.CharField(max_length=4, default=0, blank=True)
    
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
    ACCDRUNK = models.BooleanField()

    Intersection = models.CharField(max_length=150, blank=True, default = '')
    routeno = models.CharField(max_length=15, default = 0, blank=True)
    case_status = models.CharField(max_length=15, blank=True, choices = CONVERT_STAT_Choices, default = '')
    convert_case = models.CharField(max_length=15,blank=True, default = '')
    
    BRIEF_FACTS = models.CharField(max_length=500,blank=True, default = '')
    
    dri_lic_no = models.CharField(max_length=150,blank=True, default = '')
    dri_name = models.CharField(max_length=150,blank=True, default = '')
    dri_fath = models.CharField(max_length=150,blank=True, default = '')
    dri_sex = models.CharField(max_length=15, choices = SEX_Choices,blank=True,default='')
    dri_age = models.PositiveIntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)],blank=True, default= 0)
    dri_add = models.CharField(max_length=150,blank=True, default = '')
    dri_arrest = models.CharField(max_length=15,choices=ARRESTED_Choices,blank=True, default = '')
    dri_place = models.CharField(max_length=150,blank=True, default = '')
    dri_lic_date_issu = models.DateField(null=True)
    dri_lic_date_upto = models.DateField(null=True)
    dri_lic_status = models.CharField(max_length=15,blank=True, default = '')
    
    REMARK = models.CharField(max_length=500, default = '', blank=True)
    CONFIRM = models.CharField(max_length=15, default = '' ,blank=True)
    LONGITUDE = models.CharField(max_length=15, blank =  True, default = '')
    LATITUDE = models.CharField(max_length=15, blank = True, default = '')


    
    CONVERT = models.CharField(max_length=15,choices=CONVERT_Choices,default = 'No')
    CONVERT_DATE = models.DateField(null=True)
    CN_DT = models.CharField(max_length=150,blank=True, default = 0)
    
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

class injured(models.Model):
    PS = models.CharField(max_length=5)
    FIRNO = models.IntegerField()
    YEAR = models.PositiveIntegerField()
    INJSEX = models.CharField(max_length=15, choices = SEX_Choices)
    INJAGE = models.CharField(max_length = 15, choices = AGE_Choices)
    INJTYPE = models.CharField(max_length = 5, choices = INJ_TYPE_CHOICES)
    ACCID_ID = models.ForeignKey(details)

class killed(models.Model):
    PS = models.CharField(max_length=5)
    FIRNO = models.IntegerField()
    YEAR = models.PositiveIntegerField()
    SEX = models.CharField(max_length = 15, choices = SEX_Choices)
    AGE = models.CharField(max_length = 15, choices = AGE_Choices)
    TYPE = models.CharField(max_length = 20, choices = INJ_TYPE_CHOICES)
    ACCID_ID = models.ForeignKey(details)
