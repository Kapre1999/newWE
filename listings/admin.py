from django.contrib import admin
from .models import *
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','realtor','price','is_published','list_date')
    list_filter = ('realtor',)
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','price','zipcode')
    list_per_page = 20

admin.site.register(Listing,ListingAdmin)
