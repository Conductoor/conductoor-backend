from django.core.management.base import BaseCommand, CommandError
from users.models import BetaRequest, User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class Command(BaseCommand):
  help = 'Send beta requests for all parties.'

  def handle(self, *args, **kwags):
    for request in BetaRequest.objects.all():
      try:
        user = User.objects.create(email=request.email, first_name="Beta", last_name="User")
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        request.delete()

        mail = EmailMultiAlternatives(
          subject='Welcome to the Conductoor Beta',
          body=render_to_string('mails/beta_invite.txt', {'password': password}),
          from_email='noreply@conductoor.villetainio.com',
          to=[user.email],
        )

        mail.send()
      except:
        pass
