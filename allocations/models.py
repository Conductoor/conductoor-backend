from django.db import models
from phases.models import Phase
from users.models import User
from skills.models import Skill

class Allocation(models.Model):
  phase = models.ForeignKey(Phase, blank=True, null=True, related_name='allocations')
  user = models.ForeignKey(User, blank=True, null=True, related_name='allocations')
  skill = models.ForeignKey(Skill, blank=True, null=True, related_name='allocations')
  hours = models.PositiveIntegerField(default=0)

  def __unicode__(self):
    return "%d" % hours
