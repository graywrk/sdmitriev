from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: { 'widget': MDEditorWidget}
    }

admin.site.register(Post, PostAdmin)
