from django.contrib import admin
from django.urls import path

from index.views import IndexView, LocationDetailView, filter_location, voronka, save_filter_location

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path(r'location/<int:pk>', LocationDetailView.as_view(), name='location_detail'),

    path('ajax/filter_location/', filter_location, name='filter_location'),
    path('ajax/voronka/', voronka, name='voronka'),
    path('ajax/save_filter_location/', save_filter_location, name='save_filter_location'),
]