from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('data', 'Data Science'),
        ('design', 'Design'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    completed_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
