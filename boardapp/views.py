from django.shortcuts import render, HttpResponse
from django.views import generic
from boardapp.models import Board

# Create your views here.

class BoardIndex(generic.TemplateView):
    template_name = "boardapp/list_boards.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['boards'] = Board.objects.all()
        return context
