from django.contrib import admin
from blog.models import Post
from django.db import models
from mdeditor.widgets import MDEditorWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: { 'widget': MDEditorWidget}
    }

admin.site.register(Post, PostAdmin)
