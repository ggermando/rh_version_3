from django.conf.urls import url


from projet.views import ListProjet, CreateProjet, DetailsProjet

app_name = 'projet'

urlpatterns = [

    url(r"^$", ListProjet.as_view(), name="home"),
    url(r"^new/$", CreateProjet.as_view(), name="create"),
    url(r'^projet//in/(?P<pk>\d+)/$', DetailsProjet.as_view(), name="details"),
]
