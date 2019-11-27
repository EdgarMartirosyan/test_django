from django.conf.urls import url, include

from . import views



urlpatterns = [

    url(r'^filters$', views.filter),
    url(r'^view/$', views.view),
    url(r'^tags-if/$', views.tags_if),
    url(r'^tags-for/$', views.tags_for),
    url(r'^regroup/$', views.tag_regroup),
    url(r'^base/$', views.base),
    url(r'^adrian/$', views.adrian),
    url(r'^realese/$', views.realese),


]