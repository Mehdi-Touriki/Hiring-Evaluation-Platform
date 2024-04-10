from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from .models import JobOffer


def apply(request):
    return render(request, "")


class JobListView(LoginRequiredMixin, ListView):
    model = JobOffer
    template_name = "jobs/jobs.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "jobs"
    ordering = ["-date_posted"]


class JobDescriptionView(LoginRequiredMixin, ListView):
    model = JobOffer
    template_name = "jobs/description.html"
    context_object_name = "job"


class JobApplyView:
    pass


class JobDeleteView(DeleteView):
    pass


class JobCreateView(CreateView):
    pass


class JobUpdateView(UpdateView):
    pass
