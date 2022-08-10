from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, CreateView, ListView

from webapp.forms import AnswerForm
from webapp.models import Poll, Answer


class PollIndexView(ListView):
    model = Poll
    template_name = 'index.html'
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5
    paginate_orphans = 0


class PollDetailView(DetailView):
    model = Poll
    template_name = 'poll_view.html'


class AnswerCrateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer.html'
