from django.urls import path
from django.urls import include, re_path
from . import views

app_name = 'sentiment_or_emotion'

urlpatterns = [
    re_path(r'^$', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
]