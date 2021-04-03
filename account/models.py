from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser



MIN = 0
MAX = 30

class LineManager(models.Model):

    isLineManager = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f'{self.isLineManager}'


class Staff(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    firstname = models.CharField(max_length=100, null=False,blank=False)
    lastname = models.CharField(max_length=100, null=False,blank=False)
    line_manager_id = models.ForeignKey(LineManager, on_delete=models.PROTECT, null=False, blank=False)
    leave_balance = models.IntegerField(default=MAX)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.getFullName}'

    @property
    def getFullName(self):
        fullname = ''
        fname = self.firstname
        lname = self.lastname
        if (fname and lname):
            fullname = lname + ' ' + fname
            return fullname
        return fullname
