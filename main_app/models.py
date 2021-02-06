from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Writer(models.Model):
    name = models.CharField(max_length=100)
    birth = models.IntegerField()
    death = models.IntegerField()
    works = models.TextField(max_length=500)
    quote = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Will have to update; I want users to be able to upload a request for a writer to add. I do NOT want users to upload these writers themselves. I want all that to happen through the backend.
    def get_absolute_url(self):
        return reverse('detail', kwargs={'writer_id': self.id})

class Routine(models.Model):
    title = models.TextField(max_length=100)
    dawn = models.TextField(blank=True)
    sunrise = models.TextField(blank=True)
    morning = models.TextField(blank=True)
    noon = models.TextField(blank=True)
    afternoon = models.TextField(blank=True)
    evening = models.TextField(blank=True)
    sunset = models.TextField(blank=True)
    dusk = models.TextField(blank=True)
    night = models.TextField(blank=True)
    midnight = models.TextField(blank=True)
    source = models.TextField(blank=True)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for writer_id: {self.writer_id} @{self.url}"