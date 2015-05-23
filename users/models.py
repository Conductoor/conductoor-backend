from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from skills.models import Skill
from phases.models import Phase

class User(AbstractBaseUser):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  working_hours = models.FloatField(default=40)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  knows = models.ManyToManyField(Skill, blank=True, null=True, related_name="users")
  in_project = models.DateField(blank=True, null=True)
  available_hours_during_project = models.FloatField(blank=True, null=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  class Meta:
    ordering = ('created',)

  def __unicode__(self):
    return "%s %s" % (first_name, last_name)
