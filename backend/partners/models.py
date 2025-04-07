from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    tag_fields = (
        ('Sustainability', 'Sustainability'),
        ('Urban Resilience', 'Urban Resilience'),
        ('Environmental Conservation', 'Environmental Conservation'),
        ('Local Business', 'Local Business'),
        ('Sustainable Agriculture', 'Sustainable Agriculture'),
    )
    area = models.CharField(max_length=75, blank=True, null=True, choices=tag_fields)
    partner_status = models.CharField(max_length=50, blank=True, null=True)
    location = models.PointField(blank=True, null=True, srid=4326)
    image = models.ImageField(blank=True, null=True, upload_to='pictures/partners/')

    def __str__(self):
        return self.name
