from rest_framework import serializers
from .models import Phase

class PhaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phase
    fields = ('id', 'title', 'time_start', 'time_end')
