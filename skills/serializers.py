from rest_framework import serializers
from .models import Skill, SkillInPhase

class SkillInPhaseSerializer(serializers.HyperlinkedModelSerializer):
  id = serializers.ReadOnlyField(source='skill.id')
  name = serializers.ReadOnlyField(source='skill.name')

  class Meta:
    model = SkillInPhase
    fields = ('id', 'name', 'required_hours')

class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = ('id', 'name')
