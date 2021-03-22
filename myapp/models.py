from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    add_time = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(default='')
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

    
class Answer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')


class Downvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
