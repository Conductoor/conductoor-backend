from .models import User
from allocations.models import Allocation
from .serializers import UserSerializer, UserPOSTSerializer, LoginSerializer, CreateUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import workdays
import datetime

class UserList(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  User
  ====
  List all users or create a new one

  Example fields for a POST request:  
  `"email": "tainio.ville@gmail.com"`  
  `"first_name": "Ville"`  
  `"last_name": "Tainio"`  
  `"working_hours": 40` (per week)  
  `"knows": [1, 2]`
  """
  def get(self, request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = UserPOSTSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Retrieve, update or delete an user instance
  """
  def get_object(self, pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = UserPOSTSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    user = self.get_object(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class AvailableUser(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Find out if user is available or not. URL parameters required for the request:  
  `time_start=2015-05-2`  
  `time_end=2015-05-22`
  """
  def get(self, request, format=None):
    try:
      time_start = datetime.datetime.strptime(request.GET['time_start'], "%Y-%m-%d").date()
      time_end = datetime.datetime.strptime(request.GET['time_end'], "%Y-%m-%d").date()
    except MultiValueDictKeyError:
      return Response(status=status.HTTP_400_BAD_REQUEST)

    if time_start > time_end:
      return Response({'error': 'time_start was larger than time_end'},
        status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.all()
    result = []
    working_days = workdays.networkdays(time_start, time_end)

    for user in users:
      if user.in_project and time_start < user.in_project:
        # User is already in another project.
        latest_allocation = Allocation.objects.filter(user__pk=user.pk).order_by('phase__time_end')[:1]
        available_hours = working_days * user.available_hours_during_project
        result.append({"id": user.pk, "free_now": False,
          "available_hours": available_hours, "phase_id": latest_allocation[0].phase.pk})

      else:
        # User isn't allocated to any project at the moment.
        available_hours = working_days * (user.working_hours / 5.0)
        result.append({"id": user.pk, "free_now": True,
          "available_hours": available_hours})

    return Response(result)

class LoginView(APIView):
  def post(self, request, format=None):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
      if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_200_OK)

      return Response({'error': 'invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUser(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  """
  Create a new user for the application. Password will be emailed to the user.  

  Fields for the request:
  `"email": "tainio.ville@gmail.com"`  
  `"first_name": "Ville"`  
  `"last_name": "Tainio"`  
  """
  def post(self, request, format=None):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      password = User.objects.make_random_password()
      user.set_password(password)
      user.save()
      # Create an auth token for the user.
      Token.objects.get_or_create(user=user)

      # Send an email to the created user containing their password.
      mail = EmailMultiAlternatives(
        subject='Welcome to Conductoor',
        body=render_to_string('mails/welcome.txt', {'first_name': user.first_name,
          'last_name': user.last_name, 'password': password}),
        from_email='noreply@conductoor.villetainio.com',
        to=[user.email],
      )

      mail.send()
      return Response({'message': 'email sent'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
