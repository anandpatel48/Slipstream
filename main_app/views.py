from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Bets
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Slipstream(TemplateView):
    template_name = "slipstream.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bets'] = Bets.objects.all()
        return context

class BetCreate(CreateView):
    model = Bets
    fields = ['description']
    template_name = "bet_create.html"
    success_url = "/slipstream/"