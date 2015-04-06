from django.db import models
from phases.models import Phase

class Skill(models.Model):
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return "%s" % name

class SkillInPhase(models.Model):
  skill = models.ForeignKey(Skill)
  phase = models.ForeignKey(Phase)
  required_hours = models.PositiveIntegerField(default=0)
