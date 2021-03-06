from django.forms import ModelForm

from .models import Task, Assignment


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('user', 'updated', 'created')


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        exclude = ('updated', 'created', 'taken', 'task', 'uid')
