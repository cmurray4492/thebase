# Views for the Blog App
from django.shortcuts import get_object_or_404, render
from .models import BlogArticle


def index(request):
    """This is the function that provides content to the Blog Home"""
    blogs = BlogArticle.objects.order_by(
        '-blog_date_posted').filter(blog_article_active=True)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)


def blogarticle(request, blog_id, blog_slug):
    """This is the function that provides dynamic content to each job post"""
    blogarticle = get_object_or_404(BlogArticle, pk=blog_id)
    context = {
        'blogarticle': blogarticle,
        'blog_id': blog_id,
        'blog_slug': blog_slug,
    }
    return render(request, 'blog/blogarticle.html', context)
