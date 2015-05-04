from .models import Phase
from skills.models import SkillInPhase
from .serializers import PhaseSerializer, PhasePOSTSerializer, RequireSkillSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PhaseList(APIView):
  """
  List all phases or create a new one
  """
  def get(self, request, format=None):
    phases = Phase.objects.all()
    serializer = PhaseSerializer(phases, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = PhasePOSTSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
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
  Require a new skill for a phase
  """
  def post(self, request, format=None):
    serializer = RequireSkillSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
