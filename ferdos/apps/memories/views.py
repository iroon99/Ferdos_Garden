from django.shortcuts import render, redirect
from django.views import View
from .models import Memory, MemoryGallery, MemoryLike
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import MemoryForm, MemoryGalleryForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
class ShowMemories(View):
    def get(self, request):
        memories = Memory.objects.filter(is_active=True)
        memory_gallery = MemoryGallery.objects.all()
        if request.user.is_authenticated:
            memory_like_list = MemoryLike.objects.filter(user_liked_id=request.user.id).values('memory_id')
            memory_like_list_id = [memory['memory_id'] for memory in memory_like_list]
            return render(request, "memories/memories.html", {'memories':memories, 'memory_gallery':memory_gallery, 'memory_like':memory_like_list_id})
        return render(request, "memories/memories.html", {'memories':memories, 'memory_gallery':memory_gallery})
    

@method_decorator(login_required, name='dispatch')
class AddMemory(View):
    def get(self, request):
        ImageFormSet = modelformset_factory(MemoryGallery, MemoryGalleryForm, extra=3)
        image_formset = ImageFormSet(queryset=MemoryGallery.objects.none())
        memory_form = MemoryForm()
        context = {
            'memory_form':memory_form,
            'image_form':image_formset
        }
        return render(request, 'memories/add.html', context)
    
    def post(self, request):
        ImageFormSet = modelformset_factory(MemoryGallery, MemoryGalleryForm, extra=3)
        memory_form = MemoryForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)

        if memory_form.is_valid() and image_formset.is_valid():
            memory_form_data = memory_form.cleaned_data
            image_formset_data = image_formset.cleaned_data

            memory_obj = Memory.objects.create(
                memory_title = memory_form_data['memory_title'],
                memory_text = memory_form_data['memory_text'],
                user_registered = request.user
            )

            for form in image_formset_data:
                if form:
                    MemoryGallery.objects.create(
                        memory_image = form['memory_image'],
                        memory = memory_obj
                    )
        
            messages.success(request, 'درج خاطره با موفقیت انجام شد', 'success')
            return redirect("/")
    
        else:
            messages.error(request, 'اطلاعات درج شده معتبر نمی باشد', 'error')
            context = {
                'memory_form':memory_form,
                'image_form':image_formset
            }
            return render(request, 'memories/add.html', context)


@login_required
def like(request):
    if request.method == 'GET':
        memory_id = request.GET.get('memory_id')
        memory = Memory.objects.get(id=memory_id)
        likememory = MemoryLike.objects.filter(memory_id=memory.id, user_liked=request.user)
        if not likememory:
            likememory = MemoryLike(memory=memory)
            likememory.user_liked = request.user
            likememory.save()
        return HttpResponse("success")
    return HttpResponse("Unsuccess")

@login_required
def dislike(request):
    if request.method == 'GET':
        memory_id = request.GET.get('memory_id')
        likememory = MemoryLike.objects.filter(memory_id=memory_id, user_liked=request.user)
        if likememory:
            print(likememory)
            likememory.delete()
        return HttpResponse("success")
    return HttpResponse("Unsuccess")