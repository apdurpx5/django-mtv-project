from django.db import models

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    def __str__(self):
        return self.name

