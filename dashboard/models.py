from django.db import models
from django.contrib.auth.models import User

class UserLimit(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    daily_limit = models.IntegerField(default=20)
    monthly_limit = models.IntegerField(default=100)

    def __str__(self):
        return self.user.username
    

class SearchHistory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    query = models.CharField(max_length=255)

    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


