from django.db import models
from django.utils.translation import gettext_lazy as _

from extended_choices import Choices

from model_utils.models import TimeStampedModel

from apps.core.models import Base

# Create your models here.
class Task(Base, TimeStampedModel):

    STATUS_CHOICES = Choices(
        ('todo',  'todo', _('A Fazer')),
        ('doing',  'doing', _('Fazendo')),
        ('done',  'done', _('Feito'))
    )

    task_name = models.CharField(
        verbose_name=_('Nome da Tarefa'),
        max_length=40
    )

    description = models.TextField(
        verbose_name=_('Descrição'),
        max_length=500,
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        verbose_name=_('Concluída?'),
        default=False
    )

    task_status = models.CharField(
        verbose_name=_('Status da Tarefa'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.todo,
        max_length=20,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Tarefa')
        verbose_name_plural = _('Tarefas')


    def __str__(self):
        return self.task_name
