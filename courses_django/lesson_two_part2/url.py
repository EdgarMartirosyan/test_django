from django.conf.urls import url, include
from . import views

# urlpatterns = [
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/history/$', views.history),# http://localhost:5650/lesson-two-part2/50-asd/history/
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/edit/$', views.edit),
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/discuss/$', views.discuss),
#     url(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/permissions/$', views.permissions),
# ]

"""
urlpatterns = [
    url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/', include([
        url(r'^history/$', views.history),
        url(r'^edit/$', views.edit),
        url(r'^discuss/$', views.discuss),
        url(r'^permissions/$', views.permissions),
    ])),
]
"""

extra_patterns = [
     url(r'^report/$', views.report),
     url(r'^report/(?P<id>[0-9]+)/$', views.report),
]


urlpatterns = [
     url(r'blog/(page-(\d+)/)?$', views.blog_articles),  # bad   http://localhost:5650/lesson-two-part2/blog/page-2/
     url(r'comments/(?:page-(?P<page_number>\d+)/)?$',views.comments),  # good  http://localhost:5650/lesson-two-part2/comments/page-2/
     url(r'^optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}), #http://localhost:5650/lesson-two-part2/optional-args/2222/
     url(r'extra/', include(extra_patterns)),#http://localhost:5650/lesson-two-part2/extra/report/
]
