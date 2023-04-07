from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "phone_number", "country", "city", "state", "zipcode"]
    list_filter = ["country", "city", "state", "zipcode"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)
