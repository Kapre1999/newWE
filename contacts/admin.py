from django.contrib import admin
from .models import *
# Register your models here.

class Contact_Admin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing')
    list_per_page = 20

admin.site.register(Contact,Contact_Admin)
