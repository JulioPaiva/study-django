from django.contrib import admin

from .models import Email, Phone, Posts, Profile, Services, Skills


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "brand", "position")


class EmailAdmin(admin.ModelAdmin):
    list_display = ("profile", "email", "label", "is_primary")


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("profile", "number", "label", "is_primary")


class ServicesAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "description")


class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Skills, SkillsAdmin)
