from rest_framework import serializers
from .models import User
from skills.serializers import SkillSerializer

class UserSerializer(serializers.ModelSerializer):
  knows = SkillSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'knows')
