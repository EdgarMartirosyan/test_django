from django.conf.urls import url, include
from . import views
from . import forms


urlpatterns = [
     # url(r'^$', views.form),
     url(r'^$', views.ContactFormView.as_view()),
     url(r'^url-form$', views.UrlView.as_view()),
     url(r'^test-view$', views.test_view),
     url(r'^search-form/$', views.search_form ),
     url(r'^file-input/$', views.file_input ),
     url(r'^search/$', views.search),
     url(r'^add-article/$', views.add_article),
     url(r'^add-author/$', views.author_add),
]



