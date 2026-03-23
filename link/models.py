from django.db import models
from django.utils.text import slugify

def generate_unique_slug(model, name):
    base_slug = slugify(name)
    slug = base_slug
    counter = 1

    while model.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug


class Links(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    img = models.ImageField(upload_to='img')
    tg = models.CharField(max_length=150, null=True, blank=True)
    tg_akk = models.CharField(max_length=150, null=True, blank=True)
    insta = models.CharField(max_length=150, null=True, blank=True)
    youtube = models.CharField(max_length=150, null=True, blank=True)
    tiktok = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    github = models.CharField(max_length=150, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Links, self.name)  
        super().save(*args, **kwargs)