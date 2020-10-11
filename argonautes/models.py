from django.db import models


class Equipage(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return f"{self.name}"
