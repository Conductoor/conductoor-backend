from .models import Project
from .serializers import ProjectSerializer, ProjectPOSTSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProjectList(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Project
  =======
  List all projects or create a new one

  Example fields for a POST request:  
  `"title": "Conductoor"`  
  `"description": "Awesome project"`
  """
  def get(self, request, format=None):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = ProjectPOSTSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Retrieve, update or delete a project instance
  """
  def get_object(self, pk):
    try:
      return Project.objects.get(pk=pk)
    except Project.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    project = self.get_object(pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    project = self.get_object(pk)
    serializer = ProjectPOSTSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    project = self.get_object(pk)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class APIRoot(APIView):
  """
  Conductoor API
  ==============

  Docs are located at: [https://conductoor-api.herokuapp.com/docs/](https://conductoor-api.herokuapp.com/docs/)
  """
  def get(self, request):
    return Response({
      'users': reverse('users', request=request),
      'projects': reverse('projects', request=request),
      'phases': reverse('phases', request=request),
      'skills': reverse('skills', request=request),
      'allocations': reverse('allocations', request=request),
      'require-skill': reverse('require-skill', request=request),
      'available-users': reverse('available-users', request=request),
      'request-user': reverse('request-user', request=request),
      'request-beta': reverse('request-beta', request=request),
      'show-beta': reverse('show-beta', request=request)})
