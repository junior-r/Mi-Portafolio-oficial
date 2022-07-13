from django.contrib import admin
from Projects.models import Project
from Projects.forms import ProjectForm


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    form = ProjectForm
    ordering = ['id']


admin.site.register(Project, ProjectAdmin)
