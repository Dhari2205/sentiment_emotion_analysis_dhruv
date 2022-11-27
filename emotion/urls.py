from django.urls import path
from django.urls import include, re_path
from . import views

app_name = 'emotion'

urlpatterns = [
    re_path(r'^$', views.emotion_analysis, name="emotion_anaylsis"),
    re_path(r'^type/$', views.emotion_analysis_type, name="emotion_analysis_type"),
    re_path(r'^import/$', views.emotion_analysis_import, name="emotion_analysis_import"),
]