from django.urls import path
from .views import staff_detail



urlpatterns = [
    path('staff/<int:id>/<str:username>', staff_detail, name="staff-detail" ),
]