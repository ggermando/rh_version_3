from django.db import models
from django.db.models import Q


GENDER = (
    ('Feminin', 'FEMININ'),
    ('Maxculin', 'MAXCULIN')
)
ETAT_CIVIL = (
    ('Marié', 'MARIE'),
    ('Celibataire', 'CELIBATAIRE')
)

# Create your models here.

class PersonnelQuerySet(models.QuerySet):
    def search(self, query):
        if query is not None:
            query = query.strip()
            return self.filter(Q(prenom__filter=query) |
                               Q(nom__filter=query) |
                               Q(post_nom__filter=query) |
                               Q(full_name__filter=query)
                                ).distinct()
        return self


class PersonnelManager(models.Manager):
    def get_queryset(self):
        return PersonnelQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Agent(models.Model):
    
    # Identité
    nom = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    image = models.ImageField(upload_to='pass_port', default='../static/images/profile.png')
    date_de_naissance = models.CharField(max_length=30)
    sexe = models.CharField(choices=GENDER, max_length=300)
    etat_civil = models.CharField(choices=ETAT_CIVIL, max_length=300)
    nbr_enfant = models.CharField(max_length=2)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)

    # Etude
    primaire = models.CharField(max_length=300)
    secondaire = models.CharField(max_length=300)
    universitaire = models.CharField(max_length=300)
    formation = models.TextField(blank=True)
    autres = models.TextField(blank=True)
    langue = models.CharField(max_length=200)

    # Formation
    maitrise = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    centre_interet = models.CharField(max_length=300, blank=True)

    created = models.DateTimeField(verbose_name='created', auto_now_add=True)

    objects = PersonnelManager()

    def __str__(self):
        return 'personne: {}'.format(self.full_name)

    def __unicode__(self):
        return 'personne: {}'.format(self.full_name)

    @property
    def full_name(self):
        return '%s %s %s' % (self.nom, self.post_nom, self.prenom)

    class Meta:
        ordering = ['nom', 'post_nom', 'prenom']


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('agent:details', kwargs={"id": self.id})
    
    
    