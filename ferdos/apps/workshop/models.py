from django.db import models

# Create your models here.
class WorkshopStatus(models.Model):
    status_title = models.CharField(max_length=100, verbose_name='وضعیت کارگاه')
    
    def __str__(self):
        return self.status_title
    
    class Meta:
        verbose_name = "وضعیت کارگاه"
        verbose_name_plural = "وضعیت ها"
        
def upload_workshop_image(instance, filename):
    return f"workshop/{instance.id}/main-image/{filename}"
        
class Workshop(models.Model):
    workshop_title = models.CharField(max_length=300, verbose_name='عنوان')
    main_picture = models.ImageField(upload_to = upload_workshop_image, verbose_name='تصویر اصلی')
    workshop_date_time = models.DateTimeField(verbose_name='تاریخ و زمان برگزاری')
    place = models.CharField(max_length=150, verbose_name='مکان برگزاری')
    teacher = models.CharField(max_length=150, verbose_name='مدرس')
    details = models.TextField(verbose_name='جزئیات کارگاه')
    reg_guide = models.TextField(verbose_name='نحوه ثبت نام')
    workshop_report = models.TextField(verbose_name='گزارش کارگاه', blank=True, null=True)
    views = models.IntegerField(verbose_name='تعداد بازدید')
    reg_date = models.DateField(verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(verbose_name='وضعیت فعالیت')
    status = models.ForeignKey(WorkshopStatus, on_delete=models.CASCADE, verbose_name='وضعیت کارگاه')
    
    def __str__(self):
        return self.workshop_title
    
    class Meta:
        verbose_name = 'کارگاه'
        verbose_name_plural = 'کارگاه ها'


def upload_workshop_gallery(instance, filename):
    return f"workshop/{instance.workshop.id}/gallery/{filename}"

class WorkshopGallery(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, verbose_name='کارگاه')
    picture = models.ImageField(upload_to = upload_workshop_gallery)
    
    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'

