from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse("Home Page!")


def items(request):
    return HttpResponse("Welcome to localhost/items")


def special_case_2003(request):
    return HttpResponse("Welcome to  localhost/item/2003!")


def year_archive(request, a):
    return HttpResponse('Welcome to localhost/[0-9]{4}! %s' % a)


def month_archive(request, year, month):
    return HttpResponse("Welcome to  localhost/item([0-9]{4})/([0-9]{2})/")


def day_archive(request, year, month, day):
    return HttpResponse('Welcome to localhost/item/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{2})')


def show_url_param(request, year):
    return HttpResponse('welcome localhost:item/?P<year>[\w]+) %s' % year)


def page(request, num="1"):
    if num == "1":
        return HttpResponse("Вы перешли на первую страницу книги")
    else:
        return HttpResponse("Вы перешли на страниц под номером %s" % num)
