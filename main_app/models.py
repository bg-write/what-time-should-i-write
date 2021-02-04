from django.db import models
from django.urls import reverse

class Writer(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    works = models.TextField(max_length=500)
    quote = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
    # Will have to update; I want users to be able to upload a request for a writer to add. I do NOT want users to upload these writers themselves. I want all that to happen through the backend.
    def get_absolute_url(self):
        return reverse('detail', kwargs={'writer_id': self.id})

class Routine(models.Model):
    dawn = models.TextField(max_length=1000)
    sunrise = models.TextField(max_length=1000)
    morning = models.TextField(max_length=1000)
    noon = models.TextField(max_length=1000)
    afternoon = models.TextField(max_length=1000)
    evening = models.TextField(max_length=1000)
    sunset = models.TextField(max_length=1000)
    dusk = models.TextField(max_length=1000)
    night = models.TextField(max_length=1000)
    midnight = models.TextField(max_length=1000)
    source = models.TextField(max_length=1000)

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)


