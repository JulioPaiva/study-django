from django.db import models


class Profile(models.Model):
    name = models.CharField("Nome", max_length=100)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Email(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="emails"
    )
    email = models.EmailField()
    label = models.CharField(max_length=50, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Recommendation(models.Model):
    RESOURCE_TYPE = [
        ("BOOK", "Livro"),
        ("ARTICLE", "Artigo"),
        ("VIDEO", "Vídeo"),
        ("COURSE", "Curso"),
        ("COURSE", "Ferramenta"),
        ("LINK", "Link"),
        ("OTHER", "Outro"),
    ]

    title = models.CharField("Título", max_length=100)
    url = models.URLField("URL", blank=True)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.url}, {self.description}, {self.resource_type}"
