from django.urls import path
from .views import LeaveList, LeaveDetail


app_name = 'leave_api'

urlpatterns = [
    path('<int:pk>/', LeaveDetail.as_view(), name="createdetail"),
    path('', LeaveList.as_view(), name="createlist"),
]