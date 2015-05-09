from rest_framework import serializers
from .models import Phase
from skills.serializers import SkillInPhaseSerializer, SkillSerializer
from allocations.serializers import AllocationSerializer
from skills.models import Skill, SkillInPhase
from projects.models import Project

class PhaseSerializer(serializers.ModelSerializer):
  required_skills = SkillInPhaseSerializer(source='skillinphase_set', many=True)
  allocations = AllocationSerializer(many=True, read_only=True)

  class Meta:
    model = Phase
    fields = ('id', 'title', 'time_start', 'time_end', 'color', 'required_skills', 'allocations')

class PhasePOSTSerializer(serializers.HyperlinkedModelSerializer):
  project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

  class Meta:
    model = Phase
    fields = ('id', 'project', 'title', 'time_start', 'time_end', 'color')

class RequireSkillSerializer(serializers.HyperlinkedModelSerializer):
  skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all())
  phase = serializers.PrimaryKeyRelatedField(queryset=Phase.objects.all())

  class Meta:
    model = SkillInPhase
    fields = ('id', 'skill', 'phase', 'required_hours')
