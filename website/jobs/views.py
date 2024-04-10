from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Post


def apply(request):
    return render(request, "")


class JobListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "jobs/jobs.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "jobs"
    ordering = ["-date_posted"]


class JobDescriptionView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "jobs/description.html"
    context_object_name = "job"


class JobApplyView:
    pass


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter
