

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update_click_count/',
         views.update_click_count, name='update_click_count')
]
