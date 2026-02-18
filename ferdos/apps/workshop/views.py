from django.shortcuts import render
from .models import Workshop, WorkshopGallery
from django.views.generic import ListView


# Create your views here.
class ShowWorkshops(ListView):
    model = Workshop
    template_name = 'workshop/workshops.html'
    context_object_name = 'workshops'
    paginate_by = 1
    queryset = Workshop.objects.filter(is_active=True)

def showReport(request, id):
    workshop = Workshop.objects.get(id=id)
    title = workshop.workshop_title
    report = workshop.workshop_report
    pictures = WorkshopGallery.objects.filter(workshop_id=id)
    context = {
        'workshop_title' : title,
        'pictures' : pictures,
        'report' : report
    }
    return render(request, 'workshop/report.html', context)