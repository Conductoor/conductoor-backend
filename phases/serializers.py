from rest_framework import serializers
from .models import Phase
from skills.serializers import SkillSerializer
from allocations.serializers import AllocationSerializer

class PhaseSerializer(serializers.ModelSerializer):
  required_skills = SkillSerializer(many=True, read_only=True)
  allocations = AllocationSerializer(many=True, read_only=True)

  class Meta:
    model = Phase
    fields = ('id', 'title', 'time_start', 'time_end', 'color', 'required_skills', 'allocations')
