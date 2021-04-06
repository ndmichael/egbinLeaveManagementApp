from django.urls import path
from leaveapp import views as leave_views

urlpatterns = [
    path('', leave_views.index, name="app-home" ),
    path('request/', leave_views.RequestLeave, name="requestleave" ),
    path('history/', leave_views.historyList, name="history" ),
    path('howtouse/', leave_views.howToUse, name="how_to_use" ),
    path('leave_list/', leave_views.approvalList, name="all_leave" ),
    path('leave_list/<str:status>/', leave_views.approvalList, name="leave_list_by_category" ),
    path('decision/', leave_views.managerApproval, name='approval'),
]