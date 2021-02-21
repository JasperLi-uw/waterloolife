from django.contrib import admin
from .models import ThreadType, Thread

# Register your models here.
@admin.register(ThreadType)
class ThreadTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'type_name')

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'thread_type', 'author', 'created_time', 'last_update_time')