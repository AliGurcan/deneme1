from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('upload/aca', views.upload_lnotes, name='uploadLnotes'),
    path('upload/stu', views.upload_snotes, name='uploadSnotes'),
    path('snotes/pdfs', views.snotes_list, name='snotesList'),
    path('lnotes/pdfs', views.lnotes_list, name='lnotesList'),
    path('snotes/images', views.snotes_list, name='snotesList'),
    path('lnotes/images', views.lnotes_list, name='lnotesList'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)