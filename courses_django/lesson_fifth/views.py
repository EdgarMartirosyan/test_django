from django.shortcuts import render , redirect
from django.http import  HttpResponseRedirect ,HttpResponse
from . import forms
from django.core.mail import send_mail
from . import models
from django.views import generic

# Create your views here.

from django.shortcuts import render


def search_form(request):
    return render(request , 'search_form.html' , {})


def search(request):
    if request.method == "GET":
        if 'q' in request.GET:
            return HttpResponse("Вы хотели найти %s" % request.GET['q'])
        else:
            return HttpResponse("Вы отправили пустую форму")


def test_view(request):

    # return HttpResponse('welcome to %s ' %request.path)
    # return HttpResponse('host is %s' %request.get_host())
    # return  HttpResponse("Полный путь %s" %request.get_full_path())
    return  HttpResponse("Защишено  %s" %request.is_secure())


def file_input(request):
    name = request.POST['name']
    surname  = request.POST['surname']
    birth  = request.POST['birth']
    gender  = request.POST['gender']
    some_file = open("some.txt", "w")
    some_file.write("Имя :" + name + "\n")
    some_file.write("Фамилия :" + surname + "\n")
    some_file.write("Дата рождения :" + birth + "\n")
    some_file.write("Пол :" + gender + "\n")
    some_file.close()
    return HttpResponse("Данные успешно были записаны!")

# def form(request):
#
#     form_for_author1 = forms.AuthorOneForm
#     form_for_article  = forms.ArticleForm
#     form_contact  = forms.ContactForm
#     context = {
#         'form_for_author1': form_for_author1,
#          'form_for_article' : form_for_article,
#          'form_contact' : form_contact
#     }
#     return render(request , 'form.html' , context)


def author_add(request):
    form =  forms.AuthorOneForm(request.POST)
    result  = "Автор успешно добавлен %s" %request.path
    if request.method == "POST":
        if form.is_valid():
            data =  form.cleaned_data
            form.save()
            print(data)
            return HttpResponse("Автор добавлен! %s" %request.path)


def add_article(request):
    form  = forms.ArticleForm(request.POST)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        form = form.save()
        return HttpResponse("Статья добавлена!")


class ContactFormView(generic.TemplateView):
    form_for_author1 = forms.AuthorOneForm
    form_for_article  = forms.ArticleForm
    form_contact  = forms.ContactForm

    def post(self , request):
        form  = forms.ContactForm(request.POST)
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': form,

        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request , 'form.html' , context)

    def get(self , request):
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article' : self.form_for_article,
            'form_contact' : self.form_contact
        }
        return render(request , 'form.html' , context)


class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def get(self , request):
        context  = {
            'form_url': self.form_submit_url
        }
        return render(request , 'url_form.html' , context)

    def post(self , request):
        form  = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'url_form.html', context)
        return HttpResponse(form.cleaned_data.items())


