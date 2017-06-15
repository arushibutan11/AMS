# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import details,circles,roads,sections

admin.site.register(details)
admin.site.register(sections)
admin.site.register(roads)
admin.site.register(circles)
# Register your models here.
