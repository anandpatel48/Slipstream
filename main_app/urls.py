from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('slipstream/', views.Slipstream.as_view(), name = "slipstream")
]