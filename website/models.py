from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=155, blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=500, blank=False, null=True)

    def __str__(self):
        return self.title 