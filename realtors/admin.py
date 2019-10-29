from django.contrib import admin
from .models import *
# Register your models here.

class Realtor_Admin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Realtor,Realtor_Admin)