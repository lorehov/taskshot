from django.core.urlresolvers import reverse
from django.db.models import Model, CharField, TextField, DateTimeField, IntegerField, ForeignKey, EmailField
from django.contrib.auth.models import User


class Task(Model):
    title = CharField(max_length=120)
    foreword = TextField(null=True)
    description = TextField()
    time_limit = IntegerField()  # hours
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    revision = IntegerField(default=1)
    user = ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_update', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tasks'
        ordering = ['-updated']


class Assignment(Model):
    task = ForeignKey(Task)
    email = EmailField()
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)
    revision = IntegerField()
    taken = DateTimeField(null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'assignments'
        ordering = ['-created']
