from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect


def recruiter_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_recruiter:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('jobs:job_list'))

    return wrapper


def candidate_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_candidate:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('jobs:job_list'))

    return wrapper
