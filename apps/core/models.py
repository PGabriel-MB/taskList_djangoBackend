import uuid
import random

from django.db import models

# Create your models here.

def rand_code():
    return '{}.{}{}{}.{}{}{}.{}'.format(*str(int(random.uniform(10000001, 99999999))))

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, default=rand_code, verbose_name='Código', editable=False)
    
    class Meta:
        abstract = True