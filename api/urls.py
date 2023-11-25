from .views import *
from django.urls import path

urlpatterns = [
    path("advantage-list/", AdvantageListAPIView.as_view()),
    path("advantage-detail/<int:pk>/", AdvantageDetailAPIView.as_view()),
    path("article-list/", ArticleListAPIView.as_view()),
    path("article-detail/<int:pk>/", ArticleDetailAPIView.as_view()),
    path("course-list/", CourseListAPIView.as_view()),
    path("course-detail/", CourseListAPIView.as_view()),
    path("AplicationForm/", AplicationFormCreateAPIView.as_view()),
    path("AuthorDetail/<int:pk>/",AuthorDetailAPIView.as_view()),
    path("way2job/",Way2JobAPIView.as_view()),
    path("gallery/",GalleryListAPIView.as_view()),

]