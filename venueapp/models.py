from django.db import models

# Create your models here.
class VenueList(models.Model):
    content = models.TextField()
    priority = models.TextField()
    dateof = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=100)