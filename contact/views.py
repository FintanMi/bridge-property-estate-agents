from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        estate_agent_email = request.POST['estate_agent_email']

        # check if user has made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
        email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        return redirect('/listings/'+listing_id)
