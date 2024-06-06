from django.contrib import admin
from .models import Movies, WriteComment
# Register your models here.
# admin.site.register(Movies)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ["name", "recommender"]
    list_display_links = ["name", "recommender"]
    search_fields = ["name"]

    class Meta:
        model = Movies

class WriteCommentAdmin(admin.ModelAdmin):
    list_display = ["commenter"]
    list_display_links = ["commenter"]
    search_fields = ["commenter"]

    class Meta:
        model = WriteComment

admin.site.register(Movies, MoviesAdmin)
admin.site.register(WriteComment, WriteCommentAdmin)

