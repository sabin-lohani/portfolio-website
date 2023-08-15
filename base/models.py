from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100)
    copyright_year = models.PositiveIntegerField()
    site_url = models.URLField()

    def __str__(self):
        return self.site_title