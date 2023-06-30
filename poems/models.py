from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
category = [
    ('EURO', 'European'),
    ('ASIA', 'Asian'),
    ('AMERICA', 'AMERICAN'),
    ('AFRICA', 'African'),
    ('OCEANIA', 'Oceania'),
]
class Poem(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(null=True, max_length=100)
    category = models.CharField(max_length=10, choices=category, default='EURO')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('poem_detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.text