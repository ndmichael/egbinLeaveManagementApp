from django.shortcuts import render

from django.contrib.auth.views import LoginView
from account.models import Staff
from leaveapp.models import Leave

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


def staff_detail (request, id, username):
    staff = Staff.objects.get(user=id)
    leave_requested = Leave.objects.filter(user=id).count()
    accepted = Leave.objects.filter(user=id, status='approved').count()
    rejected = Leave.objects.filter(user=id, status='rejected').count()

    context = {
        'staff': staff,
        'leave_requested': leave_requested,
        'accepted': accepted,
        'rejected': rejected,
    }

    return render(request, 'account/staff_details.html', context)




