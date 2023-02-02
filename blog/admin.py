from django.contrib import admin
from .models import BlogArticle


class ListingAdmin(admin.ModelAdmin):
    """This is Admin setup for the Blog App"""
    list_display = ('id', 'blog_title', 'blog_date_posted',
                    'blog_author', 'blog_article_active')
    list_display_links = ('id', 'blog_title')
    list_editable = ('blog_article_active',)
    search_fields = ('blog_title', 'blog_article',
                     'blog_tags', 'blog_description')
    prepopulated_fields = {"blog_slug": ("blog_title",)}


admin.site.register(BlogArticle, ListingAdmin)
