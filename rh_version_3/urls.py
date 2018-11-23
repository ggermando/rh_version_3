"""rh_version_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from .views import Home, LoginView, LogoutView, Bienvenue

handler400 = 'rh_version_3.views.handler400'
handler500 = 'rh_version_3.views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agent/', include('agent.urls', namespace="agent")),
    url(r'^projet/', include('projet.urls', namespace="projet")),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'), 
    url(r'^home/$', Home.as_view(), name='home')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
