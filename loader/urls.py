from django.urls import path
from loader import views as loader
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', loader.pets, name='pets'),
    path('addpet/', loader.photo_load, name='photo_load'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# from django.urls import path
# from loader import views as loader
#
# urlpatterns = [
#     path('', loader.pets, name='pets'),
#     path('addpet/', loader.add_pet, name='photo_load'),
# ]
