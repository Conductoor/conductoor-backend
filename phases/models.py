from django.db import models

class Phase(models.Model):
  title = models.CharField(max_length=100)
  time_start = models.DateField(blank=True, null=True)
  time_end = models.DateField(blank=True, null=True)

  def __str__(self):
    return "{}".format(title)
