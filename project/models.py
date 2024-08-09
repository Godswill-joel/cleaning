from django.db import models
from account.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    created = models.DateTimeField(
        auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug= slugify(self.name)
    #        super().(save)(*args, **kwargs)


    def __str__(self):
        return f"category for {self.name}"




class Project(models.Model):
    category = models.ForeignKey(
        "project.Category", 
        verbose_name=("Project Categories"), 
           on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(User,  verbose_name=("User"), null= True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(null=True,  blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="media", null=True, blank=True)