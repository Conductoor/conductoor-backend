from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  time_start = models.DateField(null=True, blank=True)
  time_end = models.DateField(null=True, blank=True)

  class Meta:
    ordering = ('created',)

  def __unicode__(self):
    return "%s" % title
