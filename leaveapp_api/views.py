from django.shortcuts import render
from rest_framework import generics
from .serializers import LeaveSerializer
from leaveapp.models import Leave


class LeaveList (generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer


class LeaveDetail (generics.RetrieveDestroyAPIView):
    queryset = Leave.objects.all()



