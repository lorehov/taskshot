from django.conf.urls import url

from .views import index, TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    url(r'^$', index, name='index'),

    # tasks
    url(r'tasks/$', TaskList.as_view(), name='task_list'),
    url(r'tasks/add/$', TaskCreate.as_view(), name='task_add'),
    url(r'tasks/(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task_update'),
    url(r'tasks/(?P<pk>[0-9]+)/delete/$', TaskDelete.as_view(), name='task_delete'),

    # other
    # url(r'^tasks/$', views.detail, name='tasks_list'),
    # url(r'^tasks/(?P<task_id>[0-9]+)/$', TaskView.as_view(), name='task_details'),
]
