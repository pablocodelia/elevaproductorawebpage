from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from . import views

admin.autodiscover()
urlpatterns = [
    path('enviar/', views.enviar, name='enviar'), 
    path('blog/', views.blog, name='blog'),
    path('newsletter/', views.newsletter, name='newsletter'), 
    path('correo_exitoso/', views.correo_exitoso, name='correo_existoso'), 


    path('sitemap.xml', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}), 
    path('', include('djangocms_blog.taggit_urls'))]

urlpatterns += i18n_patterns(path('admin/', admin.site.urls), path('', include('cms.urls')))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.
        STATIC_ROOT)
