from django.urls import path
from .views import viewproperty_listing, agents_details_list

urlpatterns = [
    path('viewproperty_listing', viewproperty_listing, name='viewproperty_listing'),
    path('agents_details_list', agents_details_list, name='agents_details_list'),
]
