from rest_framework import serializers
from .models import User
from skills.serializers import SkillSerializer
from skills.models import Skill

class UserSerializer(serializers.ModelSerializer):
  knows = SkillSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'knows')

class UserPOSTSerializer(serializers.ModelSerializer):
  knows = serializers.PrimaryKeyRelatedField(many=True, queryset=Skill.objects.all())

  class Meta:
    model = User
    fields = ('id', 'email', 'first_name', 'last_name', 'knows')

class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(max_length=100)
