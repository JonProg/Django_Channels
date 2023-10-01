from django.db import models
from utils.rands import slugify_new

class Groups(models.Model):
    group = models.CharField(max_length=100)
    slug = models.SlugField(
        unique = True, default = None,
        null = True, blank = True, max_length = 100
    )

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.group, 4)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.group
