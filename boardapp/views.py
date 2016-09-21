from django.shortcuts import get_object_or_404
from django.views import generic
from boardapp.models import Board, Thread

# Create your views here.

class BoardIndex(generic.TemplateView):
    template_name = "boardapp/list_boards.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['boards'] = Board.objects.all()
        return context

class ThreadIndex(generic.TemplateView):
    template_name = "boardapp/list_threads.html"

    def get_context_data(self, boardname):
        context = super().get_context_data()
        board = get_object_or_404(Board, shortcut=boardname)
        context['board'] = board
        context['threads'] = Thread.objects.filter(board=board)
        # import pdb; pdb.set_trace()
        return context


class ThreadView(generic.TemplateView):
    template_name = "boardapp/view_thread.html"

    def get_context_data(self, boardname, threadid):
        context = super().get_context_data()
        thread = get_object_or_404(Thread, pk=threadid)
        context['thread'] = thread
        return context