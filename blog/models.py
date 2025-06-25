

from django.db import models

class BlogProject(models.Model):
    title = models.CharField(max_length=100)  # fixed: lowercase "title"
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='blogs-image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # fixed: consistent name
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
