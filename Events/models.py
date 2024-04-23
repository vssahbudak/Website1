from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name='Olay Adı')
    description = models.TextField(null=True, verbose_name='Olay Açıklaması')
    image = models.CharField(max_length=50,verbose_name='Olay ikonu')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Olay Tarihi')
    isClosed = models.BooleanField(default=False,verbose_name='Kapalı')

    def __str__(self):
        return self.name
    
    def get_image_path(self):
        return '/img/' + self.image