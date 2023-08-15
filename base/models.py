from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100)
    copyright_year = models.PositiveIntegerField()
    site_url = models.URLField()

    def __str__(self):
        return self.site_title

class PersonalInfo(models.Model):
    display_pic = models.ImageField(upload_to='profile_pics/')
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"