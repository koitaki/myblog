from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    filter_vertical = ()
    ordering = ('updated',)
    fields = ['title', 'slug', 'author', 'post', 'updated', 'pub_date']
    list_display = ('title', 'slug', 'author', 'post', 'updated', 'pub_date')
    list_display_links = ('title', 'slug', 'author', 'post')
    search_fields = ('title', 'slug', 'author', 'post')
    list_per_page = 25

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'post', 'text', 'created']
    list_display = ('author', 'post', 'text', 'created')
    list_display_links = ('author', 'post', 'text',)
    search_fields = ('author', 'post', 'text', 'created')
    list_per_page = 25

admin.site.register(Comment, CommentAdmin)

