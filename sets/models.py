from django.db import models

# Create your models here.
class Set(models.Model):

    CATEGORIES = (
        ('warmup', 'Warm-Up'),
        ('mainset', 'Main Set'),
        ('cooldown', 'Cool-Down'),
    )

    distance = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES, default="mainset")