from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .manager import LeaveManager
from django.urls import reverse
import datetime


# Create your models here.

LEAVE_TYPE = (
    ('SICK', 'Sick leave'),
    ('EXAM', 'Exam leave'),
    ('ANNUAL', 'Annual leave'),
    ('COMPASSIONATE', 'Compassionate leave'),
)

STATUS = (
    ('pending', 'PENDING'),
    ('approved', 'APPROVED'),
    ('rejected', 'REJECTED'),
)


class Leave (models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    startdate = models.DateField(help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(help_text='coming back on ...',null=True,blank=False)
    resumptiondate = models.DateField(help_text='coming back on ...',null=True,blank=False)
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=20, default='SICK', null=True, blank=True)
    is_approved = models.BooleanField (default=False)
    status = models.CharField(choices=STATUS, default="pending", max_length=15)

    date_approved = models.DateTimeField (auto_now_add=True)
    date_created = models.DateTimeField (auto_now_add=True)

    initial_balance = models.IntegerField(default=0)
    final_balance = models.IntegerField(default=0)

    objects = models.Manager()
    leavemanagers = LeaveManager()

    @property
    def days_requested(self):
        diff = self.enddate - self.startdate
        return f"{diff.days}"

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"{self.leavetype} {self.user}"
    
    def get_absolute_url(self):
        return reverse('leave_list_by_status', args=[ self.status])
