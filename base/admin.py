from django.contrib import admin
from .models import *

# Register your models here.

class AdvocateAdmin(admin.ModelAdmin):
    list_display = ('username','bio','id')
    search_fields = ('username','bio')

admin.site.register(Advocate,AdvocateAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','bio','uuid')
    search_fields = ('name','bio')

admin.site.register(Company,CompanyAdmin)