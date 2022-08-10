from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, CreateView, ListView

from webapp.forms import AnswerForm
from webapp.models import Poll, Answer, Choice


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        return context

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.poll_id = self.kwargs.get("pk")
        answer.save()
        return redirect("poll_index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["pk"] = self.kwargs.get("pk")
        return kwargs

    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk")
    #     poll = get_object_or_404(Poll, pk=pk)
    #     context = {"poll": poll}
    #     # context["choices"] = poll.choices.all()
    #     return render(request, "answer.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk")
    #     poll = get_object_or_404(Poll, pk=pk)
    #     choice_pk = request.POST.get("choice")
    #     choice = get_object_or_404(Choice, pk=choice_pk)
    #     Answer.objects.create(poll=poll, option=choice)
    #     return redirect("poll_index")
