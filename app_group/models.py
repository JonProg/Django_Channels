from django.db import models
from utils.rands import slugify_new

class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique = True, default = None,
        null = True, blank = True, max_length = 100
    )

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
