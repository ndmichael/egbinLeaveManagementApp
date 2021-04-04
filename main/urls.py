
from django.contrib import admin
from django.urls import path, include
from account.views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('account/', include('account.urls')),
    path('account/login/', CustomLoginView.as_view(template_name="account/login.html"), name="login"),
    path('account/logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path('', include('leaveapp.urls')),
    path('api/', include('leaveapp_api.urls', namespace='leaveapp_api')),
]
