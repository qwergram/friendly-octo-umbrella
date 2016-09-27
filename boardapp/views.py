from django.shortcuts import get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from boardapp.models import Board, Thread, Post
from boardapp import forms

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
        context['threads'] = board.threads.all()
        return context


class ThreadView(generic.TemplateView):
    template_name = "boardapp/view_thread.html"

    def get_context_data(self, boardname, threadid):
        context = super().get_context_data()
        thread = get_object_or_404(Thread, pk=threadid)
        context['thread'] = thread
        context['posts'] = thread.posts.all()
        return context

class CreateThread(generic.View):

    def post(self, request, boardname):
        form = forms.CreateThread(request.POST)
        if form.is_valid:
            board = get_object_or_404(Board, shortcut=boardname)
            new_thread = Thread(board=board)
            new_thread.save()
            new_post = Post(
                title=form.data['title'], 
                content=form.data['content'],
                password=form.data.get('deletion_password'),
                thread=new_thread,
            )
            new_post.save()
            return HttpResponseRedirect(reverse('threadView', kwargs={'boardname':boardname, 'threadid': new_thread.pk}))
        else:
            return HttpResponse("oops something went wrong")


class CreatePost(generic.View):

    def post(self, request):
        return HttpResponse('hello world!')