from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.views.genetic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):

    template_name ='index.html'

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):

form_class = PhotoPostForm
template_name = "post_photo.html"
success_url = reverse_lazy('photo:post_done')

def form_valid(self, form):
    postdata = form.save(commit=False)
    postdata.user = self.request.user
    postdata.save()
    return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'