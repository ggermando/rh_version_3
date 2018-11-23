from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, CreateView

from .utils import Render
from .models import Agent
from .forms import AgentForm
# Create your views here.

class AgentList(ListView):
    model = Agent
    template_name = 'agent/agent_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Pdf(View):
    def get(self, request, id, *args, **kwargs):
        agent = get_object_or_404(Agent, id=id)
        params = {
        'agent': agent,
        }
        return Render.render('agent/pdf.html', params)

class CreateAgent(CreateView):
    form_class = AgentForm
    model = Agent
    template_name = 'agent/new_agent.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)