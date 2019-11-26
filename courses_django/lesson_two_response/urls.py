from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.hello_response),  # localhost:5650/lesson-two-response/
    url(r'^redirect/$', views.http_redirect),  # localhost:5650/lesson-two-response/redirect
    url(r'^fun1/$', views.fun1),
    url(r'^render-html/$', views.render_html),  # localhost:5650/lesson-two-response/render-html
    url(r'^render-template/$', views.render_template),  # localhost:5650/lesson-two-response/render-template
    url(r'^render-to-response/$', views.func_render_to_response),
    # localhost:5650/lesson-two-response/render-to-response
    url(r'render-template/form-hendler/$', views.form_hendler),
]
