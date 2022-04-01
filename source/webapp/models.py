from django.db import models

# Create your models here.

STATUS_CHOICE = [('new', 'новая'), ('moderated', 'модерированная')]


class Quote(models.Model):
    text = models.TextField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][1])
    created_at = models.DateTimeField(auto_now_add=True)
