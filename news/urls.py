from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('authorlist/', AuthorList.as_view()),
    path('post/<int:pk>/', Post.as_view())
]