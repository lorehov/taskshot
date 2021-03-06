from django.conf.urls import url

from .views import (
    index, TaskList, TaskCreate, TaskUpdate, TaskDelete, AssignmentList, AssignmentCreate,
    AssignmentDelete, AssignmentPreview, AssignmentDetails
)

urlpatterns = [
    url(r'^$', index, name='index'),

    # tasks
    url(r'tasks/$', TaskList.as_view(), name='task_list'),
    url(r'tasks/add/$', TaskCreate.as_view(), name='task_add'),
    url(r'tasks/(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task_update'),
    url(r'tasks/(?P<pk>[0-9]+)/delete/$', TaskDelete.as_view(), name='task_delete'),

    # assignments
    url(r'assignments/$', AssignmentList.as_view(), name='assignment_list'),
    url(r'assignments/(?P<task_pk>[0-9]+)/$', AssignmentList.as_view(), name='assignment_list'),
    url(r'assignments/(?P<task_pk>[0-9]+)/add/$', AssignmentCreate.as_view(), name='assignment_add'),
    url(r'assignments/(?P<pk>[0-9]+)/delete/$', AssignmentDelete.as_view(), name='assignment_delete'),
    url(r'assignments/(?P<slug>[\w-]+)/preview/$', AssignmentPreview.as_view(), name='assignment_preview'),
    url(r'assignments/(?P<slug>[\w-]+)/details/$', AssignmentDetails.as_view(), name='assignment_details'),

    # other
    # url(r'^tasks/$', views.detail, name='tasks_list'),
    # url(r'^tasks/(?P<task_id>[0-9]+)/$', TaskView.as_view(), name='task_details'),
]
