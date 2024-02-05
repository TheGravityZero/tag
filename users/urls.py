from django.urls import path

from users import views
from users.views import LKView

urlpatterns = [
    path('', LKView.as_view(), name='lk'),
    path('/logout', views.logout_view, name='logout'),
    path('ajax/wishlist/', views.add_wishlist, name='ajax_wishlist'),
    path('ajax/delete_wishlist/', views.delete_wishlist, name='delete_wishlist'),
    path('ajax/change_city/', views.change_city, name='change_city'),

    path('pay/one/', views.pay_one, name='pay_one'),
    path('pay/mounth/', views.pay_mounth, name='pay_mounth'),
    path('pay/year/', views.pay_year, name='pay_year'),
    path('pay_webhook', views.pay_webhook_handler, name='pay_webhook_handler'),
    path('pay_stop', views.pay_stop, name='pay_stop')
]