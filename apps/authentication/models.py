from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel

from apps.core.models import Base

# Create your models here.
class User(Base, AbstractUser, TimeStampedModel):
    pass