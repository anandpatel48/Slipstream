from django.contrib import admin
from .models import Profile
from .models import Bets
from .models import Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Bets)
admin.site.register(Comment)
