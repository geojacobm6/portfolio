from django.contrib import admin

from models import Projects, Technologies

class ProjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Projects, ProjectsAdmin)

class TechnologiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Technologies, TechnologiesAdmin)