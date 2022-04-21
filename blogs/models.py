from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import User
# from tinymce import models as tinymce_models
# from accounts.models import Profile
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField( unique = True,blank=True)
    discription = models.TextField()

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

