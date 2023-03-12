from django.urls import path
from .views import Alert

urlpatterns = [
    path('alert/',Alert.as_view()),
]