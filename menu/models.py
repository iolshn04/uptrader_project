from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=200)