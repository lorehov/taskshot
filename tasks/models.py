import uuid

from django.core.urlresolvers import reverse
from django.db.models import (
    Model, CharField, TextField, DateTimeField, IntegerField, ForeignKey, EmailField, UUIDField, FileField
)
from django.contrib.auth.models import User


def get_attachment_path(instance, filename):
    return 'attachments/{}/{}.{}'.format(instance.id, filename, instance.uuid)


class Task(Model):
    title = CharField(max_length=120)
    foreword = TextField(null=True)
    description = TextField()
    time_limit = IntegerField()  # hours
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    user = ForeignKey(User)
    uuid = UUIDField(default=uuid.uuid4)
    attachment = FileField(upload_to=get_attachment_path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_update', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tasks'
        ordering = ['-updated']


class Assignment(Model):
    uid = UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)
    task = ForeignKey(Task)
    email = EmailField()
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    taken = DateTimeField(null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'assignments'
        ordering = ['-created']
