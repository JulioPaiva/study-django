from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Profile(Base):
    name = models.CharField("Nome", max_length=100)
    nickname = models.CharField("Apelido", max_length=40, blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    video = models.URLField(blank=True)
    brand = models.CharField("Marca", max_length=10, blank=True)
    position = models.CharField("Cargo", max_length=100, blank=True)
    bio = models.TextField(blank=True)
    message = models.TextField(max_length=200, blank=True)
    welcome_message = models.CharField(
        "Mensagem de Boas-vindas", max_length=40, blank=True
    )

    def __str__(self):
        return (
            f"{self.name}"
            f"{self.nickname}"
            f"{self.github}"
            f"{self.instagram}"
            f"{self.linkedin}"
            f"{self.video}"
            f"{self.brand}"
            f"{self.position}"
            f"{self.bio}"
            f"{self.message}"
            f"{self.welcome_message}"
        )


class Email(Base):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="emails"
    )
    email = models.EmailField()
    label = models.CharField(
        max_length=50, blank=True, help_text="Ex: Trabalho, Pessoal"
    )
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Phone(Base):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="phones"
    )
    number = models.CharField(max_length=20)
    label = models.CharField(
        max_length=50, blank=True, help_text="Ex: Trabalho, Pessoal"
    )
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class Services(Base):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="services"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skills(Base):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="stack"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
