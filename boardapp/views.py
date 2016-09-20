from django.shortcuts import render, HttpResponse
from django.views import generic
from boardapp.models import Board

# Create your views here.

class BoardIndex(generic.View):

    def get(self, request):
        boards = Board.objects.all()
        return HttpResponse(str([str(x) for x in boards]))
