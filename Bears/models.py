from django.db import models
from datetime import datetime
# Create your models here.
class Bears(models.Model):
  bear_type = models.CharField(max_length=20)
  bear_age = models.CharField(max_length=20)
  bear_count = models.IntegerField(default=1)
  sighting_date = models.DateField(default=datetime.today, blank=True)
  sighting_time = models.TimeField(default=datetime.today, blank=True)
  sighting_location = models.CharField(max_length=50)
  sighting_notes = models.CharField(max_length=200)

  def __str__(self):
    return (self.sighting_name)

  @property
  def sighting_name(self):
    return '%s %s' % (self.sighting_date, self.bear_type)