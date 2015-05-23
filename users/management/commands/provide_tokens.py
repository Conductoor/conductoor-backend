from django.core.management.base import BaseCommand, CommandError
from users.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
  help = 'Provide tokens for users'

  def handle(self, *args, **kwargs):
    for user in User.objects.all():
      Token.objects.get_or_create(user=user)
