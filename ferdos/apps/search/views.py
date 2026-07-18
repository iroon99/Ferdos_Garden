from django.shortcuts import render
from django.http import HttpResponse
from apps.memories.models import Memory
from apps.workshop.models import Workshop
from apps.blog.models import Article
from django.db.models import Q

# Create your views here.
def search(request):
    if request.method == 'GET':
        query = request.GET.get("q")
        memories = Memory.objects.filter(
            Q(memory_title__icontains=query), is_active=True
        )
        workshops = Workshop.objects.filter(
            Q(workshop_title__icontains=query)
        )
        articles = Article.objects.filter(
            Q(article_title__icontains=query)
        )
        context = {
            'memories':memories,
            'workshops':workshops,
            'articles':articles
        }
        return render(request, 'search/show.html', context)