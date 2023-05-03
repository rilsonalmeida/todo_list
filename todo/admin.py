from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ('title', 'date_completed', 'is_important', 'user', )


admin.site.register(Todo, TodoAdmin)
