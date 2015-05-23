from django.db import models
from phases.models import Phase
from users.models import User
from skills.models import Skill

import workdays
import datetime

class Allocation(models.Model):
  phase = models.ForeignKey(Phase, blank=True, null=True, related_name='allocations')
  user = models.ForeignKey(User, blank=True, null=True, related_name='allocations')
  skill = models.ForeignKey(Skill, blank=True, null=True, related_name='allocations')
  hours = models.PositiveIntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

  class Meta:
    ordering = ('created',)

  def save(self, *args, **kwargs):
    super(Allocation, self).save(*args, **kwargs)

    working_days = workdays.networkdays(self.phase.time_start, self.phase.time_end)
    user_hours_per_day = self.user.working_hours / 5.0
    project_hours_per_day = self.hours / working_days

    # Calculate working hours for the user.
    if self.user.in_project and self.user.in_project <= self.phase.time_start:
      self.user.in_project = self.phase.time_end
      if project_hours_per_day >= user_hours_per_day:
        self.user.available_hours_during_project = 0.0
      else:
        self.user.available_hours_during_project = user_hours_per_day - project_hours_per_day

    elif self.user.in_project and self.user.in_project >= self.phase.time_end:
      if project_hours_per_day >= self.user.available_hours_during_project:
        self.user.available_hours_during_project = 0.0
      else:
        self.user.available_hours_during_project = self.available_hours_during_project - project_hours_per_day

    elif self.user.in_project and self.user.in_project <= self.phase.time_end:
      self.user.in_project = self.phase.time_end
      if project_hours_per_day >= self.user.available_hours_during_project:
        self.user.available_hours_during_project = 0.0
      else:
        self.user.available_hours_during_project = self.available_hours_during_project - project_hours_per_day

    else:
      self.user.in_project = self.phase.time_end
      if project_hours_per_day >= user_hours_per_day:
        self.user.available_hours_during_project = 0.0
      else:
        self.user.available_hours_during_project = user_hours_per_day - project_hours_per_day

    self.user.save()

  def __unicode__(self):
    return "%d" % hours
