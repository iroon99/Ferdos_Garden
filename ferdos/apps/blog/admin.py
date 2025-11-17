from django.contrib import admin
from .models import Article, Author, ArticleGroup, Keyword, ArticleGallery

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'article_title',
        'author',
        'group',
        'registered_at',
        'is_active'
    ]
    
@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'article',
        'article_picture'
    ]
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'family',
        'email',
        'registered_at',
        'is_active'
    ]
    prepopulated_fields = {'slug':('name', 'family')}
    
@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name'
    ]
    
@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = [
        'keyword_name'
    ]