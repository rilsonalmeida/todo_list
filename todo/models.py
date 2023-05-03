from django.db import models
from django.contrib.auth.models import User


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Todo(TimestampableMixin):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    date_completed= models.DateTimeField(null=True, blank=True)
    is_important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
