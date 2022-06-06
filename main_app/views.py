from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse('SlipStream Home Page, this will also include information about the app')