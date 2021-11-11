from django.urls import path
from label.views import HomeView, HouseholdLabelView, EALabelView

urlpatterns = [
    path('', HomeView.as_view(), name="labelprint"),
    path('printByHousehold/', HouseholdLabelView.as_view(), name="byHousehold"),
    path('printByEA/', EALabelView.as_view(), name="byEA"),
]
