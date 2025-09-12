from django.shortcuts import render
from django.conf import settings
from .models import Place, Ticket

# Create your views here.
def history(request):
    return render(request, "about/history.html")

def parts(request):
    return render(request, "about/parts.html")

def showMuseumPlaces(request):
    places = Place.objects.all()
    context = {
        'places' : places
    }
    return render(request, "about/museum_places.html", context)

def showGardenPlaces(request):
    places = Place.objects.all()
    context = {
        'places' : places
    }
    return render(request, "about/garden_places.html", context)

def showVisitGuide(request):
    return render(request, "about/visit_guide.html")

def showVisitPlan(request):
    places = Place.objects.all()
    tickets = Ticket.objects.all()
    context = {
        'places' : places,
        'tickets' : tickets
    }
    return render(request, "about/visit_plan.html", context)
