from django.contrib import admin
from ops.models import Author, Keyword, Organization, Paper


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'organization')
    exclude = ('uid',)


class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    exclude = ('id',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Keyword)
admin.site.register(Organization)
