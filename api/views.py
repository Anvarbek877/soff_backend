from django.shortcuts import render
from . import  models
from . import serializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView, Response
from django.core.paginator import Paginator


class AdvantageListAPIView(ListAPIView):
    queryset = models.Advantage.objects.all()
    serializer_class = serializer.AdvantageListSerializer
    # filter_backends = [SearchFilter,DjangoFilterBackend, ]
    # search_fields = ("full_name", )
    # filterset_fields = ("created_at", "status", "amount", )

class AdvantageDetailAPIView(RetrieveAPIView):
    queryset = models.Advantage.objects.all()
    serializer_class = serializer.AdvantageDetailSerializer

class ArticleListAPIView(ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializer.ArticleListSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend ]
    pagination_class = LimitOffsetPagination
    search_fields = ("title", )
    filterset_fields = ("category", "author")

    def blog(request):


        posts = models.Article.objects.all()
        paginator = Paginator(posts, 1)
        page_number = request.GET.get("page")
        page_objs = paginator.get_page(page_number)

        return render(request, {"posts":page_objs})

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializer.ArticleDetailSerializer

class CourseListAPIView(ListAPIView):
    queryset =models.Course.objects.all()
    serializer_class = serializer.CourseListSerializer

class CourseDetailAPIView(RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseDetailSerializer

class AplicationFormCreateAPIView(CreateAPIView):
    queryset = models.AplicationForm.objects.all()
    serializer_class = serializer.AplicationFormSerializer


class CategoryWithCountAPIView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategoryWithCountSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializer.AuthorSerializer
    lookup_field = "pk"

class Way2JobAPIView(APIView):
    def get(self,request):
        object=Way2JobAPIView


class GalleryListAPIView(ListAPIView):
    queryset =models.Gallery.objects.all()
    serializer_class = serializer.GalerySerializer
