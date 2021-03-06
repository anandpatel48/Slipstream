from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('slipstream/', views.Slipstream.as_view(), name = "slipstream"),
    path('bets/new/', views.BetCreate.as_view(), name = "bet_create"),
    path('bets/<int:pk>', views.BetDetail.as_view(), name = "bet_detail"),
    path('bets/<int:pk>/delete', views.BetDelete.as_view(), name = "bet_delete"),
    path('bets/<int:pk>/comment/', views.CommentCreate.as_view(), name = "comment_create"),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name = "comment_delete"),
    path('bets/<int:pk>/PhotoAdd', views.PhotoAdd.as_view(), name = "photo_add"),
    path('bets/<int:bet_id>/add_photo/', views.add_photo, name = "add_photo"),
    path('profile/<int:pk>', views.Profile.as_view(), name='users-profile'),
]