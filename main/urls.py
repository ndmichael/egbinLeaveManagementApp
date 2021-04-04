
from django.contrib import admin
from django.urls import path, include
from account.views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/login/', CustomLoginView.as_view(template_name="account/login.html"), name="login"),
    path('account/logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path('', include('leaveapp.urls')),
    path('api/', include('leaveapp_api.urls', namespace='leaveapp_api')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
