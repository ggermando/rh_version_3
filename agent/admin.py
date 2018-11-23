from django.contrib import admin

from .models import Agent
# Register your models here.

admin.site.site_header = 'Sunphenix HR administraction'

admin.site.register(Agent)
