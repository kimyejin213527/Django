from django.urls import path

from shinee import views

app_name = "shinee"

urlpatterns = [
    path('taemin/', views.show_taemin, name='taemin'),
    path('on/', views.show_on, name='on'),
]