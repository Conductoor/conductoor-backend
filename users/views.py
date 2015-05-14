from .models import User
from .serializers import UserSerializer, UserPOSTSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
  """
  User
  ====
  List all users or create a new one

  Example fields for a POST request:  
  `"email": "tainio.ville@gmail.com"`  
  `"first_name": "Ville"`  
  `"last_name": "Tainio"`  
  `"knows": [1, 2]`
  """
  def get(self, request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = UserPOSTSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
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
    serializer = UserPOSTSerializer(user, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    user = self.get_object(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
