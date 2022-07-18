from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Bets
from .models import Comment
from .models import Photo
from .models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
import os
import uuid
import boto3
from botocore.exceptions import ClientError
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

@method_decorator(login_required, name = "dispatch")
class Slipstream(TemplateView):
    template_name = "slipstream.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bets'] = Bets.objects.all().reverse()
        context['photos'] = Photo.objects.all()
        return context

@method_decorator(login_required, name = "dispatch")
class BetCreate(CreateView):
    model = Bets
    fields = ['description']
    template_name = "bet_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BetCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('photo_add', kwargs = {'pk': self.object.pk})


class BetDetail(DetailView):
    model = Bets
    context_object_name = "bet"
    template_name = "bet_detail.html"

    def get_context_data(self, ** kwargs):
        context = super(BetDetail, self).get_context_data(**kwargs)
        return context


class BetDelete(DeleteView):
    model = Bets
    template_name = 'bet_delete_confirmation.html'
    success_url = '/slipstream/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['bet'] = Bets.objects.get(id = pk)
        return context

    
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment_create.html"
    
    def form_valid(self, form):
        form.instance.bet_id = self.kwargs['pk']
        form.instance.user = self.request.user
        print(form.instance.bet_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bet_detail', kwargs = {'pk': self.kwargs['pk']})

    
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comment_delete_confirmation.html'
    success_url = '/slipstream/'



def add_photo(request, bet_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            print(url)
            Photo.objects.create(url=url, bet_id=bet_id)
        except ClientError as e:
            print(f"this is the error: {e}")
    return redirect('/slipstream/')


    


class PhotoAdd(TemplateView):
    template_name = "photo_add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['bet'] = Bets.objects.get(id = pk)
        return context



