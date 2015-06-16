from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from .models import Task, Assignment
from .forms import TaskForm, AssignmentForm


def index(request):
    return render(request, 'index.html')


class _LoginRequired(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(_LoginRequired, self).dispatch(*args, **kwargs)


class TaskList(_LoginRequired, ListView):
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    model = Task


class TaskCreate(_LoginRequired, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(_LoginRequired, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.revision += 1
        return super(TaskUpdate, self).form_valid(form)


class TaskDelete(_LoginRequired, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')


class AssignmentList(_LoginRequired, ListView):
    template_name = 'tasks/assignment_list.html'
    context_object_name = 'assignments'
    model = Assignment


class AssignmentCreate(_LoginRequired, CreateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignment_list')


class AssignmentUpdate(_LoginRequired, UpdateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignment_list')


class AssignmentDelete(_LoginRequired, DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignment_list')
