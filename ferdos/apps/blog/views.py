from django.shortcuts import render
from .models import Article, ArticleGallery

# Create your views here.
def showBlogs(request):
    blogs = Article.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, "blog/blogs.html", context)

def showBlogDetail(request, id):
    blog = Article.objects.get(id=id)
    
    keywords = blog.keywords.all()
    kws = [str(kw) for kw in list(keywords)]
    kws = ','.join(kws)
    
    pictures = ArticleGallery.objects.filter(article_id = id)
    
    context = {
        'blog' : blog,
        'kws' : kws, 
        'pictures' : pictures
    }
    return render(request, 'blog/detail.html', context)