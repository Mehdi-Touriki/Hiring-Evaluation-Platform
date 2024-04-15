import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from django.http import HttpResponse
from .models import Post, ApplyJob
from users.models import User
from .form import ApplyForm, CreateJobForm
from .decorators import recruiter_required, candidate_required

from .models import ApplyJob


@recruiter_required
def post_job(request):
    return render(request, "jobs/index.html")


class JobListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = "jobs/jobs.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "jobs"
    ordering = ["-publication_data"]
    login_url = "users:login"

    def test_func(self):
        return self.request.user.is_candidate


class JobDescriptionView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "jobs/description.html"
    context_object_name = "job"
    login_url = "users:login"


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    login_url = "users:login"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter


@recruiter_required
def job_create_view(request):
    recruiter = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            print("success")
            job = form.save(commit=False)
            job.recruiter = recruiter
            job.save()
            return redirect('jobs:my_jobs')  # Redirect to the desired URL upon successful submission
        else:
            print(form.errors)
    else:
        print("method not post")
        form = CreateJobForm()
    return render(request, 'jobs/formulaire.html', {'form': form})


@candidate_required
def job_apply_view(request, pk):
    form = ApplyForm(request.POST, request.FILES)
    job = get_object_or_404(Post, id=pk)
    user = get_object_or_404(User, id=request.user.id)
    applicant = ApplyJob.objects.filter(user=user, job=pk)

    if not applicant:
        if request.method == 'POST':
            if form.is_valid():
                print("success")
                instance = form.save(commit=False)
                instance.application_name = "candidature_" + str(uuid.uuid4())
                instance.user = user
                instance.job = job
                instance.save()
                print("success")
                messages.success(request, 'You have successfully applied for this job!')
                return redirect(reverse("jobs:job_description", kwargs={'pk': pk}))  # Redirect to job description page
            else:
                print("invalid form")
                # Form is invalid, render the form again with validation errors
                return render(request, 'jobs/applyjob.html', {'form': form, 'pk': pk})
        else:
            print("not a post request")
            form = ApplyForm()
        return render(request, 'jobs/applyjob.html', {'form': form, 'pk': pk})
    else:
        print("user already applied")
        messages.error(request, 'You already applied for the Job!')
        return redirect(reverse("jobs:job_description", kwargs={'pk': pk}))


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['job_title', 'description']
    login_url = "users:login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter


class MyJobListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = "jobs/my_jobs.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "jobs"
    ordering = ["-publication_data"]
    login_url = "users:login"

    def test_func(self):
        return self.request.user.is_recruiter

    def get_queryset(self):
        # Get the queryset of all jobs
        queryset = super().get_queryset()
        # Filter the queryset to include only the jobs owned by the current recruiter
        queryset = queryset.filter(recruiter=self.request.user)
        return queryset

def requests(request):
    user = request.user
    replied_jobs = ApplyJob.objects.filter(user=user).select_related('job')
    return render(request, 'requests.html', {'replied_jobs': replied_jobs})
    