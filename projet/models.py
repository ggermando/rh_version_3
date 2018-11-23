from django.db import models
from django.utils.text import slugify

from agent.models import Agent

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template

register = template.Library()


class Projet(models.Model):
    nom_du_projet = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.CharField(max_length=255, blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    agent_membres = models.ManyToManyField(Agent)

    def __str__(self):
        return self.nom_du_projet

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom_du_projet)
        self.description_html = self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('projet:details', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["nom_du_projet"]


# membre du projet
class ProjetMember(models.Model):
    projet = models.ForeignKey(Projet, related_name="memberships")
    agent = models.ForeignKey(Agent, related_name='user_groups')

    def __str__(self):
        return self.agent.nom

    class Meta:
        unique_together = ("projet", "agent")
