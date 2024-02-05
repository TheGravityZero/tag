from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from index.views import IndexView, LK, Locate, LocationFree, LocationItem, error_view
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('accounts/', include('users.urls')),
    path('location/', Locate.as_view(), name='location'),
    path('location_free', LocationFree.as_view(), name='location_free'),
    path('location_item', LocationItem.as_view(), name='location_item'),
    path('error/', error_view, name='error'),
    path('login', views.user_login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)