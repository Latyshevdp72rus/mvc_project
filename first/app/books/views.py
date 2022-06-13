from django.shortcuts import render
from django.http import HttpResponse

def get_books_list(request):
    return HttpResponse("ЗДесь будет список книг")
