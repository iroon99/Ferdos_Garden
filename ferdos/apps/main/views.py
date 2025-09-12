from django.shortcuts import render
from .forms import ContactForm
from .models import Message

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def contactUs(request):
    context = {}
    contactForm = ContactForm(request.POST)
    submited = False
    if request.method == 'POST':
        if contactForm.is_valid():
            data = contactForm.cleaned_data
            msg = Message()
            msg.user_name = data["user_name"]
            msg.user_family = data["user_family"]
            msg.user_email = data["user_email"]
            msg.message_title = data["message_title"]
            msg.message_text = data["message_text"]
            msg.is_seen = False
            msg.save()
            
            submited = True
            contactForm = ContactForm()
    else:
        contactForm = ContactForm()

    context = {
        'contact_form':contactForm,
        'submited':submited
    }
    return render(request, "main/contact_us.html", context)
