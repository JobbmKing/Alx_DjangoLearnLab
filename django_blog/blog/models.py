from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # short text field
    content = models.TextField()  # long text field
    published_date = models.DateTimeField(auto_now_add=True)  # auto add when created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # link to User model

    def __str__(self):
        return self.title
