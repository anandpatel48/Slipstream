from django.contrib import admin
from .models import Profile
from .models import Bets
from .models import Comment
from .models import Photo
# Register your models here.
# Still need to work on profile
admin.site.register(Profile)
admin.site.register(Bets)
admin.site.register(Comment)
admin.site.register(Photo)
