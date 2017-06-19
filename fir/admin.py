# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import details,circles,roads,sections,vehtype1,vehtype2,self_type

admin.site.register(details)
admin.site.register(sections)
admin.site.register(roads)
admin.site.register(circles)
admin.site.register(vehtype1)
admin.site.register(vehtype2)
admin.site.register(self_type)
# Register your models here.
