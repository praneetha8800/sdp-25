# agents/views.py
from django.shortcuts import render


def viewproperty_listing(request):
    return render(request, 'properties/viewproperty_listing.html')

from agents.models import AgentDetail
def agents_details_list(request):
    agents_details_list = AgentDetail.objects.all()
    return render(request, 'properties/viewproperty_listing.html', {'agents_details_list': agents_details_list})
