from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

LEAVE_TYPE = (
    ('SICK', 'Sick leave'),
    ('EXAM', 'Exam leave'),
    ('ANNUAL', 'Annual leave'),
    ('COMPASSIONATE', 'Compassionate leave'),
)

STATUS = (
    ('PENDING', 'pending'),
    ('APPROVED', 'approved'),
    ('rejected', 'rejected'),
)


class Leave (models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    startdate = models.DateField(help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(help_text='coming back on ...',null=True,blank=False)
    resumptiondate = models.DateField(help_text='coming back on ...',null=True,blank=False)
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=20, default='SICK', null=True, blank=True)
    is_approved = models.BooleanField (default=False)
    status = models.CharField(choices=STATUS, default="PENDING", max_length=15)