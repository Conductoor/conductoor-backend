from rest_framework import serializers
from .models import User
from skills.serializers import SkillSerializer
from skills.models import Skill

class UserSerializer(serializers.ModelSerializer):
  knows = SkillSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'knows')

class UserPOSTSerializer(serializers.HyperlinkedModelSerializer):
  knows = serializers.HyperlinkedRelatedField(many=True, view_name='skills-detail', queryset=Skill.objects.all())

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'knows')
