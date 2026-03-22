from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Profile(Base):
    name = models.CharField("Nome", max_length=100)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    position = models.CharField("Cargo", max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}, {self.github}, {self.instagram}, {self.bio}"


class Email(Base):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="emails"
    )
    email = models.EmailField()
    label = models.CharField(max_length=50, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.email
