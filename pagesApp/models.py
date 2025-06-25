from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=100)  # fixed: lowercase "title"
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='blogs-image', null=True, blank=True)
    project_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Add the URL to your project (e.g., GitHub, live site)"
    )
    created_at = models.DateTimeField(auto_now_add=True)  # fixed: consistent name
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'