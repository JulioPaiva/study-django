from django.contrib import admin

from .models import Email, Newsletter, Phone, Post, Profile, Service, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "brand", "position")


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("profile", "number", "label", "is_primary")


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "description")


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
