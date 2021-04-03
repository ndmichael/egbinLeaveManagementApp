from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from django.contrib import messages

# Create your views here.

@login_required
def index (request):
    return render(request, 'leaveapp/index.html')


def RequestLeave (request):

    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave_form = form.save(commit=False)
            leave_form.user = request.user
            leave_form.save()
            messages.success(request, f'Leave submitted for {request.user.username}')
            return redirect('app-home')
    else:
        form = LeaveForm()

    return render(request, 'leaveapp/leaverequest.html', {'form':form})


def ApprovalList (request):
    pass