from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView
from projet.models import Projet, ProjetMember
from . import models


class CreateProjet(CreateView):
    fields = ("nom_du_projet", "description", "agent_membres")
    model = Projet

class DetailsProjet(DetailView):
    model = Projet

class ListProjet(ListView):
    model = Projet
