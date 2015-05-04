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

class AllocationPOSTSerializer(serializers.HyperlinkedModelSerializer):
  user = serializers.HyperlinkedIdentityField(view_name='users-detail')
  phase = serializers.HyperlinkedIdentityField(view_name='phases-detail')
  skill = serializers.HyperlinkedIdentityField(view_name='skills-detail')

  class Meta:
    model = Allocation
    fields = ('id', 'phase', 'user', 'skill', 'hours')
