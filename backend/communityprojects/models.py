from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


# Create your models here.
class CommunityProjects(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    tags = (
        ('Sustainability', 'Sustainability'),
        ('Urban Reselience', 'Urban Reselience'),
        ('Environmental Conservation', 'Environmental Conservation'),
        ('Local Business', 'Local Business'),
        ('Sustainable Agriculture', 'Sustainable Agriculture'),
    )
    area = models.CharField(max_length=20, blank=True, null=True)
    location = models.PointField(blank=True, null=True, srid=4326)
