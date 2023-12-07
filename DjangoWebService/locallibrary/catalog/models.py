from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid


class Thread(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    def get_absolute_url(self):
        return reverse('thread', kwargs={'thread_slug': self.slug})


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    