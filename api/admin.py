from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)

admin.site.register(Course)

admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('id','full_name','position')
    list_display_links = ('id','title')
    search_fields = ('full_name')
    list_filter=('full_name','position')
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('id','title','created_at','category')
    list_display_links = ("id","title")
    search_fields = ('title',)
    list_filter=('category','created_at','author')
admin.site.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_filter = ('id','title','tags','poster')
    list_display_links = ('id','title')
    search_fields = ('title')
admin.site.register(AplicationForm)
admin.site.register(Gallery)
admin.site.register(Tag)
#admin.site.register(Way2job)

@admin.register(Way2job)
class Way2jobAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Way2job.objects.exists():
            return False
        return True

    def has_delete_permission(self,request, obj=None):
        if Way2job.objects.exists():
            return False
        return  True