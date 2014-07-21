from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, Context

from models import Projects, Technologies

def home(request, template='home.html'):
    data = {}
    projects = Projects.objects.all()
    skills = Technologies.objects.all()
    data['projects'] = projects
    data['skills'] = skills
    return render_to_response(template,data,context_instance=RequestContext(request))
    