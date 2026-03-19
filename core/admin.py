from django.contrib import admin

from .models import Email, Profile, Recommendation


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")


class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("title", "resource_type", "created_at")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
