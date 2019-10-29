from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail

# Create your views here.
def contact(requset):
    if requset.POST:
        name = requset.POST['name']
        listing = requset.POST['listing']
        email = requset.POST['email']
        phone = requset.POST['phone']
        message = requset.POST['message']
        listing_id = requset.POST['listing_id']
        userId = requset.POST['userId']
        realtor_email = requset.POST['realtor_email']

        if requset.user.is_authenticated:
            userId = requset.POST['userId']
            has_contected = Contact.objects.all().filter(listing_id=listing_id,user_id=userId)
            if has_contected:
                messages.error(requset,"You Have Already Made an Inquire for this property")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id,name=name,email=email,listing=listing,phone=phone,message=message,user_id=userId)
        contact.save()

        send_mail(
            'Property Listing Enqurie',
            'There Has Been a Inquery at Btre For Your Listig' + listing + 'Sing in to admin panel to check',
            'From',
            ['to'],
            fail_silently=False
        )

        messages.success(requset,"Your Request has Been Submitted")

        return redirect('/listings/'+listing_id)
    else:
        return redirect('index')
