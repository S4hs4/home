from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    creator = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " | " + self.year + " | " + self.creator


