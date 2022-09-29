from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    id=models.IntegerField(primary_key=True)
    task_name=models.CharField(max_length=200)
    date_created=models.DateTimeField(default=datetime.now)
    completed=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name


class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username


