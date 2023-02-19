from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Question, Post
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'text']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url=reverse_lazy('home')


def demo(request):
    return HttpResponse("Hello World!!!")


def detail(request, question_id):
    HttpResponse("You're looking at %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of questions %s"
    HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('member/index.html')
    content = {
        'lastest_question_list': lastest_question_list,
    }
    return HttpResponse(template.render(content, request))
