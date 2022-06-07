from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)


class Bets(models.Model):
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    bet = models.ForeignKey(Bets, related_name = "comments", on_delete = models.CASCADE, default = 1)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    content = models.CharField(max_length = 280)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_at']

        def __str__(self):
            return '%s - %s' % (self.post.content, self.user)

