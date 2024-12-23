from http.client import HTTPResponse

from django.shortcuts import render



def test_page(request):
    return HTTPResponse('Hello world')

