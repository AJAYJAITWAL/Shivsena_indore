from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #using for mediafile uploading
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='index'),
    path('admin/', admin.site.urls),
    path('sena/',include('membership.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
	  # using for upload image as well as this is mandatory when we uploding image 
