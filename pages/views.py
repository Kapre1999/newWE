from django.shortcuts import render
from django.http import HttpResponse
from listings.models import *
from realtors.models import *
from listings.choices import *
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'beedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choice
    }
    return render(request,'pages/index.html',context)

def aboutus(request):
    relators = Realtor.objects.order_by('-hire_date')

    is_mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':relators,
        'mvp_realtor':is_mvp
    }

    return render(request,'pages/about.html',context)