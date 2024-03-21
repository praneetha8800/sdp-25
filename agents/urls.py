from django.contrib import admin
from django.urls import path
from .views import property_listing, add_agents_details, view_agents_details

urlpatterns = [
    path('property_listing/', property_listing, name='property_listing'),
    path('add_agents_details/', add_agents_details, name='add_agents_details'),
    path('view_agents_details/', view_agents_details, name='view_agents_details'),
]
