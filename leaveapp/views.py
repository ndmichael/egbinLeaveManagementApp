from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from django.contrib import messages
from leaveapp.models import Leave
from account.models import Staff
from django.http import JsonResponse, HttpResponse
import datetime

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


def historyList (request):
    leaves = Leave.objects.all().filter(is_approved=True)

    context = {
        'leaves': leaves,
    }

    return render(request, 'leaveapp/history.html', context)


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
        leave_obj = get_object_or_404(Leave, id=id)
        staff_obj = get_object_or_404(Staff, user=leave_obj.user)
        print("staff obj", staff_obj)
        days_num = leave_obj
        leavetype = leave_obj.leavetype

        # manager decision
        
        if decision == 'approved' or decision == 'rejected':
            leave_obj.is_approved = True
            leave_obj.status = decision
            leave_obj.date_approved = datetime.date.today()
            staff_obj.leave_balance_old = staff_obj.leave_balance
            staff_obj.leave_balance -= int(leave_obj.days_requested)
            leave_obj.save()
            staff_obj.save()

        return JsonResponse({'id': id, 'decision': decision, 'staff': staff_obj.leave_balance})
    return HttpResponse("Error access denied")
