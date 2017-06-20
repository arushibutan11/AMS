# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
SEX_Choices = (
    ('M','Male'),('F','Female'),
)
CONVERT_Choices=(
    ('T','TRUE'),('F','FALSE'),)
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

class vehtype1(models.Model):
    VEHTYPE = models.CharField(max_length=20, primary_key= True)
    VEHDETL = models.CharField(max_length=20)
    VEHDTL = models.CharField(max_length=40)
    SIMPLE = models.CharField(max_length=10,null =True)
    NONINJ = models.CharField(max_length=10,null=True)
    FATAL = models.CharField(max_length=10,null = True)
    PERINJ = models.CharField(max_length=10,null = True)
    PERKIL = models.CharField(max_length=10,null = True)
    PEDESTRIAN= models.CharField(max_length=10,null = True)
    CARI= models.CharField(max_length=10,null = True)
    CARK= models.CharField(max_length=10,null = True)
    DTCI= models.CharField(max_length=10,null = True)
    DTCK= models.CharField(max_length=10,null = True)
    BLBI= models.CharField(max_length=10,null = True)
    BLBK= models.CharField(max_length=10,null = True)
    BUSI= models.CharField(max_length=10,null = True)
    BUSK= models.CharField(max_length=10,null = True)
    OSBI= models.CharField(max_length=10,null = True)
    OSBK= models.CharField(max_length=10,null = True)
    MBSI= models.CharField(max_length=10,null = True)
    MBSK= models.CharField(max_length=10,null = True)
    TAXI= models.CharField(max_length=10,null = True)
    TAXK= models.CharField(max_length=10,null = True)
    TSRI= models.CharField(max_length=10,null = True)
    TSRK= models.CharField(max_length=10,null = True)
    TWWI= models.CharField(max_length=10,null = True)
    TWWK= models.CharField(max_length=10,null = True)
    MILI= models.CharField(max_length=10,null = True)
    MILK= models.CharField(max_length=10,null = True)
    DLVI= models.CharField(max_length=10,null = True)
    DLVK= models.CharField(max_length=10,null = True)
    TRCI= models.CharField(max_length=10,null = True)
    TRCK= models.CharField(max_length=10,null = True)
    POVI= models.CharField(max_length=10,null = True)
    POVK= models.CharField(max_length=10,null = True)
    AMBI= models.CharField(max_length=10,null = True)
    AMBK= models.CharField(max_length=10,null = True)
    STRI= models.CharField(max_length=10,null = True)
    STRK= models.CharField(max_length=10,null = True)
    TMPI= models.CharField(max_length=10,null = True)
    TMPK= models.CharField(max_length=10,null = True)
    MATI= models.CharField(max_length=10,null = True)
    MATK= models.CharField(max_length=10,null = True)
    TNKI= models.CharField(max_length=10,null = True)
    TNKK= models.CharField(max_length=10,null = True)
    UNKI= models.CharField(max_length=10,null = True)
    UNKK= models.CharField(max_length=10,null = True)
    CYCI= models.CharField(max_length=10,null = True)
    CYCK= models.CharField(max_length=10,null = True)
    TNGI= models.CharField(max_length=10,null = True)
    TNGK= models.CharField(max_length=10,null = True)
    CYRI= models.CharField(max_length=10,null = True)
    CYRK= models.CharField(max_length=10,null = True)
    HDCI= models.CharField(max_length=10,null = True)
    HDCK= models.CharField(max_length=10,null = True)
    BULI= models.CharField(max_length=10,null = True)
    BULK= models.CharField(max_length=10,null = True)
    ANII= models.CharField(max_length=10,null = True)
    ANIK= models.CharField(max_length=10,null = True)
    CRNI= models.CharField(max_length=10,null = True)
    CRNK= models.CharField(max_length=10,null = True)
    UDTI= models.CharField(max_length=10,null = True)
    UDTK= models.CharField(max_length=10,null = True)
    PEDI= models.CharField(max_length=10,null = True)
    PEDK= models.CharField(max_length=10,null = True)
    HTVI= models.CharField(max_length=10,null = True)
    HTVK= models.CharField(max_length=10,null = True)
    SLFI= models.CharField(max_length=10,null = True)
    SLFK= models.CharField(max_length=10,null = True)
    ELTI= models.CharField(max_length=10,null = True)
    ELTK= models.CharField(max_length=10,null = True)
    WLLI= models.CharField(max_length=10,null = True)
    WLLK= models.CharField(max_length=10,null = True)
    PASI= models.CharField(max_length=10,null = True)
    PASK= models.CharField(max_length=10,null = True)
    def __str__(self):
        return self.VEHDETL

class vehtype2(models.Model):
    VEHTYPE=models.CharField(max_length=30, primary_key= True)
    VEHDETL=models.CharField(max_length=20)
    VEHDTL = models.CharField(max_length=40)
    SIMPLE= models.CharField(max_length=10,null = True)
    NONINJ= models.CharField(max_length=10,null = True)
    FATAL= models.CharField(max_length=10,null = True)
    PERINJ= models.CharField(max_length=10,null = True)
    PERKIL= models.CharField(max_length=10,null = True)
    PEDESTRIAN= models.CharField(max_length=10,null = True)
    CARI= models.CharField(max_length=10,null = True)
    CARK= models.CharField(max_length=10,null = True)
    DTCI= models.CharField(max_length=10,null = True)
    DTCK= models.CharField(max_length=10,null = True)
    BLBI= models.CharField(max_length=10,null = True)
    BLBK= models.CharField(max_length=10,null = True)
    BUSI= models.CharField(max_length=10,null = True)
    BUSK= models.CharField(max_length=10,null = True)
    OSBI= models.CharField(max_length=10,null = True)
    OSBK= models.CharField(max_length=10,null = True)
    MBSI= models.CharField(max_length=10,null = True)
    MBSK= models.CharField(max_length=10,null = True)
    TAXI= models.CharField(max_length=10,null = True)
    TAXK= models.CharField(max_length=10,null = True)
    TSRI= models.CharField(max_length=10,null = True)
    TSRK= models.CharField(max_length=10,null = True)
    TWWI= models.CharField(max_length=10,null = True)
    TWWK= models.CharField(max_length=10,null = True)
    MILI= models.CharField(max_length=10,null = True)
    MILK= models.CharField(max_length=10,null = True)
    DLVI= models.CharField(max_length=10,null = True)
    DLVK= models.CharField(max_length=10,null = True)
    TRCI= models.CharField(max_length=10,null = True)
    TRCK= models.CharField(max_length=10,null = True)
    POVI= models.CharField(max_length=10,null = True)
    POVK= models.CharField(max_length=10,null = True)
    AMBI= models.CharField(max_length=10,null = True)
    AMBK= models.CharField(max_length=10,null = True)
    STRI= models.CharField(max_length=10,null = True)
    STRK= models.CharField(max_length=10,null = True)
    TMPI= models.CharField(max_length=10,null = True)
    TMPK= models.CharField(max_length=10,null = True)
    MATI= models.CharField(max_length=10,null = True)
    MATK= models.CharField(max_length=10,null = True)
    TNKI= models.CharField(max_length=10,null = True)
    TNKK= models.CharField(max_length=10,null = True)
    UNKI= models.CharField(max_length=10,null = True)
    UNKK= models.CharField(max_length=10,null = True)
    CYCI= models.CharField(max_length=10,null = True)
    CYCK= models.CharField(max_length=10,null = True) 
    TNGI= models.CharField(max_length=10,null = True)
    TNGK= models.CharField(max_length=10,null = True)
    CYRI= models.CharField(max_length=10,null = True)
    CYRK= models.CharField(max_length=10,null = True)
    HDCI= models.CharField(max_length=10,null = True)
    HDCK= models.CharField(max_length=10,null = True)
    BULI= models.CharField(max_length=10,null = True)
    BULK= models.CharField(max_length=10,null = True)
    ANII= models.CharField(max_length=10,null = True)
    ANIK= models.CharField(max_length=10,null = True)
    CRNI= models.CharField(max_length=10,null = True)
    CRNK= models.CharField(max_length=10,null = True)
    UDTI= models.CharField(max_length=10,null = True)
    UDTK= models.CharField(max_length=10,null = True)
    PEDI= models.CharField(max_length=10,null = True)
    PEDK= models.CharField(max_length=10,null = True)
    HTVI= models.CharField(max_length=10,null = True)
    HTVK= models.CharField(max_length=10,null = True)
    SLFI= models.CharField(max_length=10,null = True)
    SLFK= models.CharField(max_length=10,null = True)
    ELTI= models.CharField(max_length=10,null = True)
    ELTK= models.CharField(max_length=10,null = True)
    WLLI= models.CharField(max_length=10,null = True)
    WLLK= models.CharField(max_length=10,null = True)
    PASI= models.CharField(max_length=10,null = True)
    PASK= models.CharField(max_length=10,null = True)
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

    FIRNO = models.IntegerField()

    SECTION = models.ForeignKey(sections)

    TIME_OCC = models.TimeField()
    TIME_TYPE = models.CharField(max_length=15, choices = TIME_TYPE_CHOICES)
    DATE_OCC = models.DateField()
    PLACE_OCC = models.CharField(max_length=140)

    ROAD = ChainedForeignKey(
        roads,
        chained_field = "CIRCLE",
        chained_model_field = "CIRCLE",
        show_all=False,
        auto_choose=True,
        sort=True)

    ROADNAME = models.CharField(max_length=150)
    LOCATION = models.CharField(max_length=140)
    CATEGORY = models.CharField(max_length=140)
    VEHTYPE1 = models.ForeignKey(vehtype1)
    TWW1 = models.CharField(max_length=15)
    RNOV1A = models.CharField(max_length=15)
    RNOV1B = models.CharField(max_length=10)
    VEHTYPE2 = models.ForeignKey(vehtype2)
    TWW2 = models.CharField(max_length=15)
    RNOV2A = models.CharField(max_length=10)
    RNOV2B = models.CharField(max_length=4)
    SELF_TYPE = models.ForeignKey(self_type)
    INJURED = models.PositiveIntegerField()
    INJMALE = models.PositiveIntegerField()
    INJFEMALE = models.PositiveIntegerField()
    INJBOY = models.PositiveIntegerField()
    INJGIRL = models.PositiveIntegerField()
    KILLED = models.PositiveIntegerField()
    KILMALE = models.PositiveIntegerField()
    KILFEMALE = models.PositiveIntegerField()
    KILBOY = models.PositiveIntegerField()
    KILGIRL = models.PositiveIntegerField()
    PEDESTRIAN = models.PositiveIntegerField()
    ACCTYPE = models.CharField(max_length=20)
    ACCID_TYPE = models.CharField(max_length=100)
    VICTIM = models.CharField(max_length=100)
    DUPL = models.CharField(max_length=15)
    PENDING = models.CharField(max_length=15)
    DAY_NIGHT = models.CharField(max_length=15)
    YEAR = models.PositiveIntegerField()
    TIME_SLOT = models.CharField(max_length=15)
    MONTH = models.CharField(max_length=15)
    FN = models.CharField(max_length=15)
    ACCAGE = models.CharField(max_length=15)
    ACCSEX = models.CharField(max_length=15, choices = SEX_Choices)
    ACCDRUNK = models.BooleanField()
    Intersection = models.CharField(max_length=150)
    routeno = models.CharField(max_length=15,null=True)
    case_status = models.CharField(max_length=15)
    convert_case = models.CharField(max_length=15)
    BRIEF_FACTS = models.CharField(max_length=500)
    dri_lic_no = models.CharField(max_length=150)
    dri_name = models.CharField(max_length=150)
    dri_fath = models.CharField(max_length=150)
    dri_sex = models.CharField(max_length=15, choices = SEX_Choices)
    dri_age = models.PositiveIntegerField()
    dri_add = models.CharField(max_length=150)
    dri_arrest = models.CharField(max_length=15,choices=ARRESTED_Choices)
    dri_place = models.CharField(max_length=150)
    dri_lic_date_issu = models.DateField()
    dri_lic_date_upto = models.DateField()
    dri_lic_status = models.CharField(max_length=15)
    REMARK = models.CharField(max_length=300)
    CONFIRM = models.CharField(max_length=15)
    LONGITUDE = models.CharField(max_length=15)
    LATITUDE = models.CharField(max_length=15)
    CONVERT = models.CharField(max_length=15,choices=CONVERT_Choices)
    CONVERT_DATE = models.DateField()
    CN_DT = models.CharField(max_length=150)
    CONVERT_FN = models.CharField(max_length=150)
    BUS_NO = models.CharField(max_length=15)
    BLACK_SPOT = models.CharField(max_length=15)
    BLACK_SPOT_NO = models.CharField(max_length=15)
    FOR_BLK = models.CharField(max_length=15)
    STATUS = models.CharField(max_length=15)
    F_STATUS = models.CharField(max_length=15)
    dri_add1 = models.CharField(max_length=15)
    RIDER_HELMET = models.CharField(max_length=15)
    PILLION_HELMET = models.CharField(max_length=15)
    STATE = models.CharField(max_length=15)
    SCANNED = models.CharField(max_length=15)
    HIT_AND_RUN_UPDATE1 = models.CharField(max_length=15)

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

