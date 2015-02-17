from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'agencyProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^about/', views.about, name='about'),
    url(r'^campaigns/', views.campaigns, name='campaigns'),
    url(r'^campaigns_pages/',views.campaigns_pages, name='campaigns_pages'),
    url(r'^splash/', views.splash, name='splash'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


