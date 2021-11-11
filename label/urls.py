from django.urls import path
from label.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="labelprint"),
]
