from django.urls import path
from .views import ShowWorkshops, showReport

urlpatterns = [
    path('', ShowWorkshops.as_view()),
    path('report/<int:id>/', showReport),
]