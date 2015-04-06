from django.db import models
from projects.models import Project

class Phase(models.Model):
  title = models.CharField(max_length=100)
  time_start = models.DateField(blank=True, null=True)
  time_end = models.DateField(blank=True, null=True)
  project = models.ForeignKey(Project, blank=True, null=True, related_name="phases")
  required_skills = models.ManyToManyField("skills.Skill", through="skills.SkillInPhase", blank=True, null=True, related_name="phases")

  def __unicode__(self):
    return "%s" % title
