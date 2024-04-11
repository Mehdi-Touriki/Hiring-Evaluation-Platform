from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import Post, Apply_job


@login_required
def post_job(request):
    return render(request, "jobs/index.html")


def apply(request):
    return render(request, "")


class JobListView(ListView):
    model = Post
    template_name = "jobs/jobs.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "jobs"
    ordering = ["-publication_data"]


class JobDescriptionView(DetailView):
    model = Post
    template_name = "jobs/description.html"
    context_object_name = "job"


class JobDeleteView(DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter


class JobCreateView(CreateView):
    model = Post
    fields = ['job_title', 'description']
    template_name = "jobs/formulaire.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobApplyView(CreateView):
    model = Apply_job
    fields = ['cv', 'email', 'name']
    template_name = "jobs/applyjob.html"


class JobUpdateView(UpdateView):
    model = Post
    fields = ['job_title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter
