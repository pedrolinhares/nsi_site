from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.projects.models import Project
from apps.members.models import Participation


def show_all(request):
    projects = Project.objects.all().order_by('status', 'start_date')
    return render_to_response(
        'show_all_projects.html',
        {'projects': projects, 'project_count': len(projects)},
        context_instance=RequestContext(request)
    )

def show_project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    participations = Participation.objects.all()
    return render_to_response(
        'show_project.html',
        {'project': project, 'participations': participations},
        context_instance=RequestContext(request)
    )
        

