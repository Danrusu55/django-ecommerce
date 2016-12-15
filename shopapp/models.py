from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import os

# Create your models here

class Product(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='pictures', blank=True, null=True)

    def post(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title
