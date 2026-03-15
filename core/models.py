from django.db import models


class Profile(models.Model):
    name = models.CharField('Nome', max_length=100)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    bio = models.TextField()


class Email(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='emails'
    )
    email = models.EmailField()
    label = models.CharField(max_length=50, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.email
