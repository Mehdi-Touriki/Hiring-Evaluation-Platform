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
from .models import (
    ApplyJob,
    Profil,
    SavedPostt,
    Post,
    ApplyJob,
    JOB_CATEGORIES)
from users.models import User
from .form import ApplyForm, CreateJobForm, profilupdate
from .decorators import recruiter_required, candidate_required
from CV_analyser import score
from django.views.generic import View


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
    success_url = reverse_lazy("jobs:my_jobs")

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
    return render(request, 'jobs/formulaire.html', {'form': form, 'job_categories': JOB_CATEGORIES})


@candidate_required
def job_apply_view(request, pk):
    form = ApplyForm(request.POST, request.FILES)
    job = get_object_or_404(Post, id=pk)
    user = get_object_or_404(User, id=request.user.id)
    applicant = ApplyJob.objects.filter(user=user, job=pk)

    if not applicant:
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit=False)
                instance.application_name = "candidature_" + str(uuid.uuid4())
                instance.user = user
                instance.job = job
                job_description = job.requirements + job.description
                file = request.FILES['cv']
                # instance.score = score.ai_score("neural_network/neural_network_1layer.keras", file, job_description, job.job_category)
                instance.score = score.static_score(file, job_description, job.job_category)
                instance.save()
                messages.success(request, 'You have successfully applied for this job!')
                return redirect(reverse("jobs:job_description", kwargs={'pk': pk}))  # Redirect to job description page
            else:
                print("invalid form")
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
    fields = [
        'job_category',
        'job_title',
        'job_type',
        'job_location',
        'description',
        'salary',
        'publication_data',
        'requirements'
    ]
    login_url = "users:login"
    template_name = "jobs/formulaire.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.recruiter

    def get_object(self, queryset=None):
        # Retrieve the existing job instance
        return get_object_or_404(Post, pk=self.kwargs['pk'], recruiter=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:  # Check if object exists (update mode)
            context['mode'] = 'Update'  # Set mode to 'Update'
        else:  # If object doesn't exist (create mode)
            context['mode'] = 'Create'  # Set mode to 'Create'
        return context


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


class AllApplicants(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ApplyJob
    template_name = "jobs/applicantsposted.html"
    context_object_name = "users"
    ordering = ["-score"]
    login_url = "users:login"

    def test_func(self):
        return True

    def get_queryset(self):
        queryset = super().get_queryset()
        job_id = self.kwargs.get('pk')
        job = get_object_or_404(Post, pk=job_id)
        queryset = queryset.filter(job=job)
        return queryset


class Myrequest(LoginRequiredMixin, ListView):
    model = ApplyJob
    template_name = "jobs/requests.html"
    context_object_name = "jobs"
    ordering = ["-job"]


# update profil
@candidate_required
def profil(request):
    if request.method == 'POST':
        p_form = profilupdate(request.POST, instance=request.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect("jobs:profil")
    else:
        p_form = profilupdate(instance=request.user)

    context = {'p_form': p_form}

    return render(request, 'jobs/profil.html', context)


class saved_post(LoginRequiredMixin, View):
    def post(self, request):
        # Get the job_id from the request data
        job_id = request.POST.get('job_id')

        # Retrieve the post object based on the job_id
        job = get_object_or_404(Post, pk=job_id)

        # Check if the user has already saved this post
        if SavedPostt.objects.filter(user=request.user, saved_post=job).exists():
            saved_post_instance = SavedPostt.objects.get(user=request.user, saved_post=job)

            # Remove the job from saved_post
            saved_post_instance.delete()

            return redirect(reverse("jobs:job_list"))

            # If the post hasn't been saved by the user, create a new SavedPostt instance and save it
        saved_post = SavedPostt(user=request.user, saved_post=job)
        saved_post.save()

        # Return a JSON response indicating success
        return redirect(reverse("jobs:job_list"))


# hada tzad bax ybyin lina liste dyl les saves
class MysaveJobListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = SavedPostt
    template_name = "jobs/my_saves.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    login_url = "users:login"

    def test_func(self):
        return self.request.user.is_candidate

    def get_queryset(self):
        # Get the queryset of all jobs
        queryset = super().get_queryset()
        # Filter the queryset to include only the jobs owned by the current recruiter
        queryset = queryset.filter(user=self.request.user)
        return queryset


CATEGORY_MAP = {v: k for k, v in JOB_CATEGORIES}


@candidate_required
def category(request, category_name):
    category_name = category_name.replace("-", " ")
    category_key = CATEGORY_MAP.get(category_name)

    if not category_key:
        messages.error(request, 'That category does not exist!!')
        return redirect("home")

    jobs = Post.objects.filter(job_category=category_key)

    return render(request, "jobs/jobs.html", {"jobs": jobs, "category": category_name})


@candidate_required
def category_list(request):
    categories = [c[1].replace(" ", "-") for c in JOB_CATEGORIES]
    return render(request, "jobs/category.html", {"categories": categories})
