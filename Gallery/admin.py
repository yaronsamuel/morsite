from django.contrib import admin
from Gallery.models import GalleryImage
from orderedmodel import OrderedModelAdmin

    
class GalleryImageAdmin(OrderedModelAdmin):
    
    list_display = ('title',
                    'image_short_name' , 
                    'homepage',
                    'gallery',
                    'description',
                    'reorder',
          )
    fields = ('item_picture' , 
                'title',
                'description',
                'homepage',
                'gallery',
          )
          
         

admin.site.register(GalleryImage, GalleryImageAdmin)
