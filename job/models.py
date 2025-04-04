from django.db import models 
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# create function to upload image
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return f"jobs/{instance.id}.{extension}"

# Create your models here.
class Job(models.Model): # table
    title = models.CharField(max_length=100) # column
    # location
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # logic
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply_job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
