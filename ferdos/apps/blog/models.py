from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    family = models.CharField(max_length=20, blank=False, null=False)
    study_degree = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.family

class ArticleGroup(models.Model):
    group_name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.group_name

class Keyword(models.Model):
    keyword_name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.keyword_name

class Article(models.Model):
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE)
    group = models.ForeignKey(ArticleGroup, blank=True, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=80, null=False, blank=False)
    article_main_picture = models.FileField(upload_to='attachments/articles')
    article_abstract = models.TextField()
    article_text = models.TextField()
    keywords = models.ManyToManyField(Keyword, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(blank=False, null=False, default="defult")
    views = models.IntegerField()
    main_file = models.FileField(upload_to='attachments/articles/files', default="")
    
    def __str__(self):
        return self.article_title
    
class Score(models.Model):
    score = models.IntegerField(blank=False, null=False) # Needs validator
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)

class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    article_picture = models.FileField(upload_to='attachments/articles/gallery')
