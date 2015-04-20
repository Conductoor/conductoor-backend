from django.db import models
from projects.models import Project

class Phase(models.Model):
  title = models.CharField(max_length=100)
  time_start = models.DateField(blank=True, null=True)
  time_end = models.DateField(blank=True, null=True)
  color = models.CharField(max_length=100, blank=True, null=True)
  project = models.ForeignKey(Project, blank=True, null=True, related_name="phases")
  required_skills = models.ManyToManyField("skills.Skill", through="skills.SkillInPhase", blank=True, null=True, related_name="phases")
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

  class Meta:
    ordering = ('created',)

  def save(self, *args, **kwargs):
    super(Phase, self).save(*args, **kwargs)

    try:
      if not self.project.start and self.time_start:
        self.project.start = self.time_start
      if not self.project.end and self.time_end:
        self.project.end = self.time_end

      if self.project.start > self.time_start:
        self.project.start = self.time_start
      if self.project.end < self.time_end:
        self.project.end = self.time_end

      self.project.save()
    except Exception as e:
      print(e)

  def __unicode__(self):
    return "%s" % title
