from django.db import models

# Create your models here.
class AgentDetail(models.Model):
    property_title = models.CharField(max_length=255)
    property_cost = models.CharField(max_length=255)
    property_type = [
        ('Residential', 'residential'),
        ('Commercial', 'commercial'),
        ('Industrial','industrial'),

    ]
    property_type = models.CharField(max_length=20, choices = property_type)
    benefits = models.TextField()
    listing = models.CharField(max_length=255)
    property_location = models.CharField(max_length=255)
    property_requirements= models.TextField()