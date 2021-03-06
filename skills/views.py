from .models import Skill
from .serializers import SkillSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class SkillList(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Skill
  =====
  List all skills or create a new one

  Example fields for a POST request:  
  `"name": "Python"`
  """
  def get(self, request, format=None):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = SkillSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkillDetail(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Retrieve, update or delete an skill instance
  """
  def get_object(self, pk):
    try:
      return Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    skill = self.get_object(pk)
    serializer = SkillSerializer(skill)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    skill = self.get_object(pk)
    serializer = SkillSerializer(skill, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    skill = self.get_object(pk)
    skill.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
