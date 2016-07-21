from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.

class BoardIndex(generic.View):

    def get(self, request):
        return HttpResponse("ok!")
