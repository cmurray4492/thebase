# This is the models file for Blog
from datetime import datetime
from django.db import models
from tinymce.models import HTMLField


class BlogArticle(models.Model):
    """This is the data model for blog article """
    blog_title = models.CharField(max_length=255)
    blog_subtitle = models.CharField(max_length=255, default="")
    blog_tags = models.CharField(max_length=255)
    blog_slug = models.SlugField(unique=True, default="")
    blog_article = HTMLField(blank=True)
    blog_description = models.CharField(max_length=175, default="")
    blog_image = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")
    blog_card_image = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default="")
    blog_date_posted = models.DateTimeField(default=datetime.now, blank=True)
    blog_article_active = models.BooleanField(default=False)
    blog_author = models.CharField(max_length=150)

    def __str__(self):
        return self.blog_slug
