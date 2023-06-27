from django.contrib import admin
from django.urls import path
from poems import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('poems/<int:id>', views.poem_detail, name='poem_detail'),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

