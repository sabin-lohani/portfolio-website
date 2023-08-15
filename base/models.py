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
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta():
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    institution_name = models.CharField(max_length=100)
    degree_title = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta():
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree_title} from {self.institution_name}"

class Testimonial(models.Model):
    author_pic = models.ImageField(upload_to='testimonial_pics/')
    author_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.author_name}"

class Award(models.Model):
    award_details = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.award_details

class NavLink(models.Model):
    link_title = models.CharField(max_length=100)
    section_link = models.CharField(max_length=100)

    def __str__(self):
        return self.link_title
    
class FaIcon(models.Model):
    platform_name = models.CharField(max_length = 150)
    icon_class = models.CharField(max_length = 150)

    def __str__(self):
        return f'{self.platform_name} - {self.icon_class}'
    
class SocialLink(models.Model):
    fa_icon = models.ForeignKey(FaIcon, on_delete=models.SET_NULL, null=True)
    link = models.URLField()

    def __str__(self):
        return f'{self.fa_icon.platform_name} - {self.link}'