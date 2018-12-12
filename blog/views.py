from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post

# Create your views here.
class HomeViewPage(ListView):
    model=Post
    template_name= 'home.html'
    context_object_name = 'list_of_posts'

class DetailViewPage(DetailView):
    model=Post
    template_name= 'post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name= 'post_new.html'
    fields= '__all__'

class UpdatePostViewPage(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields= ['title','content']