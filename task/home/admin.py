from django.contrib import admin
from .models import portfolio

class CVAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]
    list_display_links = ["name", "surname"]
    search_fields = ["name"]

    class Meta:
        model = portfolio

admin.site.register(portfolio, CVAdmin)
