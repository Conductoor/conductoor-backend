from rest_framework import serializers
from .models import Project
from phases.serializers import PhaseSerializer
from allocations.serializers import AllocationSerializer

class ProjectSerializer(serializers.ModelSerializer):
  phases = PhaseSerializer(many=True, read_only=True)

  class Meta:
    model = Project
    fields = ('id', 'title', 'time_start', 'time_end', 'description', 'phases',)

class ProjectPOSTSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'title', 'description')
