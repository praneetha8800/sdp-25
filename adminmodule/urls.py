from django.contrib import admin
from django.urls import path, include
from . import views  # Make sure to import your views correctly

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('properties/', views.propertieshomepage, name='propertieshomepage'),
    path('agents/', views.agentshomepage, name='agentshomepage'),
    path('signup/', views.signup, name='signup'),  # Make sure to use trailing slashes for consistency
    path('signup1/', views.signup1, name='signup1'),
    path('login/', views.login, name='login'),
    path('login1/', views.login1, name='login1'),
    path('logout/', views.logout, name='logout'),

    # Add feedback URL pattern
    path('feedback_form/', views.feedback_form_view, name='feedback_form'),  # Assuming feedback_view is your feedback form view
    path('thank-you/', views.admin_thank_you_view, name='admin_thank_you'),
]
