from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^items$', views.items, name="items"),  # http://localhost:5650/items
    url(r'^item/2003/$', views.special_case_2003, name="special_case_2003"),  # http://localhost:5650/item/2003/
    url(r'^item/([0-9]{4,5})/$', views.year_archive, name="year_archive"),  # http://localhost:5650/item/1234/
    url(r'^item/([0-9]{4})/([0-9]{2})$', views.month_archive, name="month_archive"),
    # http://localhost:5650/item/2017/10
    url(r'^item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})/$', views.day_archive, name="day_archive"),
    # http://localhost:5650/item/2000/01/05/
    url(r'^item/(?P<year>[\w]+)$', views.show_url_param, name="show_url_param"),
    # http://localhost:5650/item/adsadasdasd
    url(r'book/$', views.page, name="page"),
    url(r'book/page(?P<num>[0-9]+)/$', views.page, name="page"),
    # url(r'^form_hendler$' , views.form_hendler , name = "form_hendler"),
    url(r'^$', views.home)
]
