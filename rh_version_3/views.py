from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.conf import settings


def handler404(request):
    return render(request, 'errors/404.html', {}, status=404)

def handler500(request):
    return render(request, 'errors/500.html', {}, status=500)


class Home(TemplateView):
    template_name ='pages/home.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #             return HttpResponseRedirect(reverse("index"))
    #     return super().get(request, *args, **kwargs)

class Bienvenue(TemplateView):
    template_name ='pages/bienvenue.html'

class LoginView(TemplateView):

    template_name = 'pages/index.html'

    def post(self, request, **kwargs):

        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):

    template_name = 'pages/index.html'

    def get(self, request, **kwargs):

        logout(request)

        return render(request, self.template_name)
