from .models import Allocation
from .serializers import AllocationSerializer, AllocationPOSTSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AllocationList(APIView):
  """
  Allocation
  ==========
  List all allocations or create a new one

  Example fields for a POST request:  
  `"user": 1`  
  `"phase": 1`  
  `"skill": 1`  
  `"hours": 40`  
  """
  def get(self, request, format=None):
    allocations = Allocation.objects.all()
    serializer = AllocationSerializer(allocations, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = AllocationPOSTSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllocationDetail(APIView):
  """
  Retrieve, update or delete an allocation instance
  """
  def get_object(self, pk):
    try:
      return Allocation.objects.get(pk=pk)
    except Allocation.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    allocation = self.get_object(pk)
    serializer = AllocationSerializer(allocation)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    allocation = self.get_object(pk)
    serializer = AllocationPOSTSerializer(allocation, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    allocation = self.get_object(pk)
    allocation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
