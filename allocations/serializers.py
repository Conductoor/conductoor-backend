from rest_framework import serializers
from .models import Allocation
from users.serializers import UserSerializer
from skills.serializers import SkillSerializer
from users.models import User
from phases.models import Phase
from skills.models import Skill

class AllocationSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  skill = SkillSerializer()

  class Meta:
    model = Allocation
    fields = ('id', 'phase', 'user', 'skill', 'hours')

class AllocationPOSTSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  phase = serializers.PrimaryKeyRelatedField(queryset=Phase.objects.all())
  skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all())


  class Meta:
    model = Allocation
    fields = ('id', 'phase', 'user', 'skill', 'hours')
