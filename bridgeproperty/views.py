from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, province_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'province_choices': province_choices
    }
    return render(request, 'bridgeproperty/index.html', context)


def about(request):
    estate_agent = Realtor.objects.order_by('name')
    top_seller = Realtor.objects.all().filter(top_seller=True)
    context = {
        'estate_agent': estate_agent,
        'top_seller': top_seller
    }
    return render(request, 'bridgeproperty/about.html', context)
