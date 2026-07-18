from django.urls import path
from .views import ShowMemories, AddMemory, like, dislike

urlpatterns = [
    path('', ShowMemories.as_view()),
    path('add/', AddMemory.as_view()),
    path('like/', like),
    path('dislike/', dislike)
]