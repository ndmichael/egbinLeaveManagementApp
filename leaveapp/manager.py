from django.db import models
import datetime

class LeaveManager(models.Manager):

    def get_queryset(self):
        '''
            returns all leaves
        '''
        return super().get_queryset()

    def pending_queryset(self):
        '''
            returns all pending leaves, desc order

        '''
        return super().get_queryset().filter(status='pending').order_by('-date_created')

    def accepted_leave(self):
        '''
            returns approved, desc order
        '''
        return super().get_queryset().filter(status='approved').order_by('-date_created')


    def rejected_leave(self):
        '''
            returns all rejected, desc order
        '''
        return super().get_queryset().filter(status='rejected').order_by('-date_created')

    def current_year(self):
        return super().get_queryset().filter(startdate__year = datetime.date.today().year)