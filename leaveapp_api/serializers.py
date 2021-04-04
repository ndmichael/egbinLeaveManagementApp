from rest_framework import serializers
from leaveapp.models import Leave


class LeaveSerializer (serializers.ModelSerializer):

    class Meta:
        model = Leave
        fields = ('id', 'startdate', 'enddate', 'resumptiondate', 'leavetype')


class DetailView (serializers.ModelSerializer):
    pass