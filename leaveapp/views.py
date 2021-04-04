from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from django.contrib import messages
from leaveapp.models import Leave
from account.models import Staff
from django.http import JsonResponse
from django.utils import timezone
import datetime

# Create your views here.


def index (request):
    return render(request, 'leaveapp/index.html')


@login_required
def RequestLeave (request):

    if request.method == 'POST':
        # if request.user.staff.balance < 
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


@login_required
def historyList (request):
    leaves = Leave.objects.all().filter(is_approved=True).order_by('-date_approved')

    context = {
        'leaves': leaves,
    }

    return render(request, 'leaveapp/history.html', context)


@login_required
def approvalList (request, status=None):
    if status:
        all_leaves = Leave.objects.all().filter(status=status)
    else:
        all_leaves = Leave.objects.all()

    return render(request, 'leaveapp/approving_list.html', {'all_leaves':all_leaves})


def managerApproval (request):
    SICK = 10
    ANNUAL = 14
    COMPASSION = 3
    EXAM = 5
    if request.POST.get('action') == 'post':
        id = request.POST.get('leave_id')
        decision = request.POST.get('decision')
        leave = get_object_or_404(Leave, id=id)
        staff_obj = get_object_or_404(Staff, user=leave.user)
        print("staff obj", staff_obj)
        days_num = leave
        leavetype = leave.leavetype

        # manager decision
        
        if decision == 'approved' or decision == 'rejected':
            leave.is_approved = True
            leave.status = decision
            leave.date_approved = timezone.now()
            leave.initial_balance = staff_obj.leave_balance
            staff_obj.leave_balance -= int(leave.days_requested)
            leave.final_balance = staff_obj.leave_balance
            leave.save()
            staff_obj.save()

        return JsonResponse({'id': id, 'decision': decision, })
    return HttpResponse("Error access denied")
