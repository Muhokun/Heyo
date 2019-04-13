from django.urls import path
from .views import *

urlpatterns = [
    path('detect_emotion/', emotion_detector)
]