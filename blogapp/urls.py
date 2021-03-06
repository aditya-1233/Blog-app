from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)


urlpatterns=[
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>",PostDetailView.as_view(),name="detail-view"),
    path("post/new",PostCreateView.as_view(),name="create-view"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="update-view"),
    path("user/<str:username>",UserPostListView.as_view(),name="user-posts"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(),name="delete-view"),
    path("about/",views.about, name="blog-about")]
