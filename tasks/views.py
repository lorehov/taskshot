from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'index.html')


class _LoginRequired(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(_LoginRequired, self).dispatch(*args, **kwargs)


class TaskList(ListView):
    template_name = 'tasks/list.html'
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
