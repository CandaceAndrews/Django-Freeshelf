from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    location = models.CharField(blank=True, null=True, max_length=100)
    favorites = models.ManyToManyField(to='Resource')

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Resource(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to="Category", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
