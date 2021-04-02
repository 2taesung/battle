from django.contrib import admin
from .models import Head, Comment, Subject, Community

# Register your models here.

admin.site.register(Head)
admin.site.register(Comment)
admin.site.register(Subject)
admin.site.register(Community)
