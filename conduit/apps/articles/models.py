from django.db import models
from django.conf import settings
from conduit.apps.core.models import TimestampedModel


class Article(TimestampedModel):
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    author = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='articles'
    )

    tags = models.ManyToManyField(
        'articles.Tag', related_name='articles'
    )
    
    #price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    #buyers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'profiles.Profile', related_name='comments', on_delete=models.CASCADE
    )


class Tag(TimestampedModel):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag
