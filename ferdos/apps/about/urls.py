from django.urls import path
from .views import history, parts, showMuseumPlaces, showGardenPlaces, showVisitGuide, showVisitPlan

urlpatterns = [
    path('history/', history),
    path('parts/', parts),
    path('museum-places/', showMuseumPlaces),
    path('garden-places/', showGardenPlaces),
    path('visit-guide/', showVisitGuide),
    path('visit-plan/', showVisitPlan)
]
