from rest_framework import serializers
from .models import Allocation
from users.serializers import UserSerializer
from skills.serializers import SkillSerializer

class AllocationSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  skill = SkillSerializer()

  class Meta:
    model = Allocation
    fields = ('id', 'phase', 'user', 'skill', 'hours')
