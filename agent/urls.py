from . import views
from django.conf.urls import url

from agent.views import AgentList, CreateAgent, Pdf


app_name = 'agent'

urlpatterns = [
    url(r'^$', AgentList.as_view(), name="home"),
    url(r'^agent/(?P<id>\d+)/$', Pdf.as_view(), name="details"),
    url(r'new_agent/$', CreateAgent.as_view(), name="create"),
]
