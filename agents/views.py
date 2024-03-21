# views.py
from django.shortcuts import render
from .models import AgentDetail

def property_listing(request):
    return render(request, 'agents/property_listing.html')

def add_agents_details(request):
    if request.method == 'POST':
        property_title = request.POST.get('property_title')
        property_cost = request.POST.get('property_cost')
        property_type = request.POST.get('property_type')
        benefits = request.POST.get('benefits')
        listing = request.POST.get('listing')
        property_location = request.POST.get('property_location')
        property_requirements = request.POST.get('property_requirements')

        agents_details = AgentDetail(
            property_title=property_title,
            property_cost=property_cost,
            property_type=property_type,
            benefits=benefits,
            listing=listing,
            property_location=property_location,
            property_requirements=property_requirements,
        )
        agents_details.save()
        return render(request, 'agents/datainserted.html')

    return render(request, 'agents/property_listing.html')

def view_agents_details(request):
    agents_details_list = AgentDetail.objects.all()
    return render(request, 'agents/view_agents_details.html', {'agents_details_list': agents_details_list})
