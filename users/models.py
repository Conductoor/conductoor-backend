from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from skills.models import Skill
from phases.models import Phase
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class ConductoorUserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None):
    if not email:
      raise ValueError('User must have an email address')
    if not first_name:
      raise ValueError('User must have a first name')
    if not last_name:
      raise ValueError('User must have a last name')

    user = self.model(
        email=ConductoorUserManager.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
      )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password):
    user = self.create_user(email, first_name, last_name, password=password)
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  working_hours = models.FloatField(default=40)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  knows = models.ManyToManyField(Skill, blank=True, null=True, related_name="users")
  in_project = models.DateField(blank=True, null=True)
  available_hours_during_project = models.FloatField(blank=True, null=True)

  objects = ConductoorUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  class Meta:
    ordering = ('created',)

  def __unicode__(self):
    return "%s %s" % (first_name, last_name)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
