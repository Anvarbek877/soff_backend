from rest_framework import serializers
from . import models
from datetime import datetime


class AdvantageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advantage
        fields = "__all__"
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields="__all__"
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields="__all__"
class CategorySeralizer(serializers.ModelSerializer):
    class   Meta:
        model=models.Category
        fields="__all__"
class AdvantageDetailSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True)
    class Meta:

        model = models.Advantage
        exclude=("body")



class ArticleListSerializer(serializers.ModelSerializer):
    diff = serializers.SerializerMethodField(method_name="difference")
    tags = TagSerializer(many=True)
    category=CategorySeralizer(many=True)
    author=AuthorSerializer(many=True)

    def difference(self, obj):
        result = obj.created_at
        r = datetime.now().date() - result
        return r

    class Meta:
        model = models.Article
        fields = ("poster",
                  'id',
                  "title",
                  "category",
                  "tags",

                  "created_at",
                  "author",
                  "diff",
                  )


class ArticleDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category=CategorySeralizer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = models.Article
        fields = ("body",
                  "author",
                  )


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ("name",
                  "body",
                  )
class AplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AplicationForm
        fields=("__all__")
class CategoryWithCountSerializer(serializers.ModelSerializer):
    count=serializers.SerializerMethodField()
    def get_count(self, obj):
        return models.Article.objects.filter(category=obj).count()
    class Meta:
        model=models.Category
        fields=("id","name","count")

class Way2jobSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Way2job
        fields=("title","body")

class GalerySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Gallery
        fields="__all__"