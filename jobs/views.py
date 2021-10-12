from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JobPost, Application
from users.models import Lecture
from .forms import AddApplicationForm, LectureApplicationForm, LectureProfileForm, JobPostForm
from django.contrib import messages


def jobs(request):
    posts = JobPost.objects.all()
    context = {'jobs': posts}
    return render(request, 'jobs/jobs.html', context)


def job(request, pk):
    post = JobPost.objects.get(id=pk)
    context = {'job': post}
    return render(request, 'jobs/detailjob.html', context)


@login_required(login_url='login')
def lectureProfile(request):
    l_profile = Lecture.objects.get(user=request.user)
    post = l_profile.jobpost_set.all()
    context = {'l_profile': l_profile, 'jobs': post}
    return render(request, 'jobs/lectureprofile.html', context)


@login_required(login_url='login')
def editLProfile(request):
    l_profile = Lecture.objects.get(user=request.user)
    form = LectureProfileForm(instance=l_profile)

    if(request.method == 'POST'):
        form = LectureProfileForm(
            request.POST, request.FILES, instance=l_profile)
        if(form.is_valid()):
            form.save()
            return redirect('l_profile')

    context = {'form': form}
    return render(request, 'jobs/l_profileform.html', context)


@login_required(login_url='login')
def addJob(request):
    l_profile = Lecture.objects.get(user=request.user)
    form = JobPostForm()

    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.author = l_profile
            job.save()
            messages.success(request, 'Job was added successfully!')
            return redirect('l_profile')

    context = {'form': form}
    return render(request, 'jobs/job_form.html', context)


@login_required(login_url='login')
def updateJob(request, pk):
    l_profile = Lecture.objects.get(user=request.user)
    job = l_profile.jobpost_set.get(id=pk)
    form = JobPostForm(instance=job)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job was updated successfully!')
            return redirect('l_profile')

    context = {'form': form}
    return render(request, 'jobs/job_form.html', context)


@login_required(login_url='login')
def deleteJob(request, pk):
    l_profile = Lecture.objects.get(user=request.user)
    job = l_profile.jobpost_set.get(id=pk)

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job was deleted successfully!')
        return redirect('l_profile')

    context = {'object': job}
    return render(request, 'jobs/job_form.html', context)


@login_required(login_url='login')
def approvedJobs(request):
    applications = Application.objects.all()
    unreadCount = applications.filter(is_approved=False).count()
    context = {'applications': applications, 'unreadCount': unreadCount}
    return render(request, 'jobs/approvedjob.html', context)


@login_required(login_url='login')
def approvedJob(request, pk):
    profile = Lecture.objects.get(user=request.user)
    application = Application.objects.get(id=pk)
    form = LectureApplicationForm(instance=application)

    if application.is_approved == False:
        application.is_approved = True
        application.save()

    if request.method == 'POST':
        form = LectureApplicationForm(request.POST, instance=application)
        if form.is_valid():
            job = form.save()
            job.is_checked = profile
            job.save()
            messages.success(request, 'Checked successfully')
            return redirect('approvedJobs')

    context = {'application': application, 'form': form}
    return render(request, 'jobs/singleApp.html', context)


@login_required(login_url='login')
def addApp(request):
    profile = Lecture.objects.get(user=request.user)
    form = AddApplicationForm()

    if request.method == 'POST':
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            app = form.save()
            app.is_checked = profile
            app.save()
            messages.success(request, 'Add Application successfully')
            return redirect('approvedJobs')

    context = {'form': form}
    return render(request, 'jobs/addapp.html', context)
