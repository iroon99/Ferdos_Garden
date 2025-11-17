from django.urls import path
from .views import showBlogs,showBlogDetail

urlpatterns = [
    path('', showBlogs),
    path('<int:id>/', showBlogDetail),
]
