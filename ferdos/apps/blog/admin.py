from django.contrib import admin
from .models import Article, Author, ArticleGroup, Keyword

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
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'family',
        'email',
        'registered_at',
        'is_active'
    ]
    
@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'editor_name'
    ]
    
@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = [
        'keyword_name'
    ]