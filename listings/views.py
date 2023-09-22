from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, province_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        kw = request.GET['keywords']
        if kw:
            queryset_list = queryset_list.filter(description__icontains = kw)

    # town
    if 'town' in request.GET:
        town = request.GET['town']
        if town:
            queryset_list = queryset_list.filter(town__iexact = town)

    # province
    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset_list = queryset_list.filter(province__iexact = province)
    
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'province_choices': province_choices,
        'listings': queryset_list,
    }
    return render(request, 'listings/search.html', context)
