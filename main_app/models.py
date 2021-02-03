from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    works = models.TextField(max_length=250)
    quote = models.TextField(max_length=500)

    def __str__(self):
        return self.name
