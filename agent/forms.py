from django import forms
from agent.models import Agent

from . import models

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'nom', 'post_nom', 'prenom', 'image', 'date_de_naissance', 'sexe', 'etat_civil', 'nbr_enfant', 'phone',
            'email', "adresse", 'primaire', 'secondaire', 'universitaire', 'formation', 'autres', 'langue', 'maitrise',
            'experience', 'reference', 'centre_interet')      

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["nom"].queryset = ()

    def redirect_url(self):
        return 

