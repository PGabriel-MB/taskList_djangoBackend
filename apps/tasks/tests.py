from django.test import TestCase

from .models import Task
# Create your tests here.
class TaskTestCase(TestCase):

    def setUp(self):
        Task.objects.create(
            task_name="Tarefa teste",
            description='Testar a funcionalidade do método str'
        )

    def test_str_return(self):
        t1 = Task.objects.get(task_name='Tarefa teste')
        self.assertEquals(t1.__str__(), 'Tarefa teste')