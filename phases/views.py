from .models import Phase
from skills.models import SkillInPhase
from .serializers import PhaseSerializer, PhasePOSTSerializer, RequireSkillSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

class PhaseList(APIView):
  """
  Phase
  =====
  List all phases or create a new one

  Example fields for a POST request:  
  `"title": "Design phase"`  
  `"project": 1`  
  `"time_start": "2015-04-22"`  
  `"time_end": "2015-04-23"`  
  `"color": "#FFFFFF"`  
  ```
  "required_skills": [
  {
    "skill": 1,
    "required_hours": 40
  }]
  ```
  """
  def get(self, request, format=None):
    phases = Phase.objects.all()
    serializer = PhaseSerializer(phases, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    required_skills = ''
    if 'required_skills' in request.data:
      required_skills = request.data['required_skills']
      request.data.pop('required_skills')

    serializer = PhasePOSTSerializer(data=request.data)
    if serializer.is_valid():
      phase = serializer.save()

      # Add required_skills as an own Serializer
      if required_skills:
        required_dict = required_skills[0]
        required_dict['phase'] = phase.pk

        required_serializer = RequireSkillSerializer(data=required_dict)
        if required_serializer.is_valid():
          required_serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(required_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhaseDetail(APIView):
  """
  Retrieve, update or delete a phase instance
  """
  def get_object(self, pk):
    try:
      return Phase.objects.get(pk=pk)
    except Phase.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    phase = self.get_object(pk)
    serializer = PhaseSerializer(phase)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    phase = self.get_object(pk)
    serializer = PhasePOSTSerializer(phase, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    phase = self.get_object(pk)
    phase.delete()
    return Response(status=status.HTTP_204_NO_CLIENT)

class RequireSkill(APIView):
  """
  RequireSkill
  ============
  Require a new skill for a phase.

  Unlike other POST requests, RequireSkill takes in foreign keys instead of url's.

  Example fields for a POST request:  
  `"skill": 1`  
  `"phase": 1`  
  `"required_hours": 40`
  """
  def post(self, request, format=None):
    serializer = RequireSkillSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
