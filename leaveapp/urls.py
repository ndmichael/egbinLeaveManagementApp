from django.urls import path
from .views import index, RequestLeave

urlpatterns = [
    path('', index, name="app-home" ),
    path('request/', RequestLeave, name="requestleave" ),
]