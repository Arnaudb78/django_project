from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

# class Comment(models.Model):
#      # champs automatique
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     comment = models.CharField(max_length=255)


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Tags(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Mot clef"
        verbose_name_plural = "Mot clefs"


class Articles(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Brouillon"
        PUBLISHED = "PB", "Publié"
        CLOSED = "CL", "Fermé"

    # champs automatique
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # champs table
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    title = models.CharField(max_length=255)
    content = models.TextField("Contenu", blank=True)
    published_at = models.DateTimeField(
        verbose_name="Date de publication", default=timezone.now, blank=True
    )

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tags, blank=True)

    # image
    thumb = models.ImageField(upload_to="images/%Y/%m/", blank=True)
    cover = models.ImageField(upload_to="images/%Y/%m/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_at", "title"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"
