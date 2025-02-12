from django.contrib import admin
from .models import *

class IncorrectInline(admin.StackedInline):
    model = Incorrect
    extra = 1

class CorrectAdmin(admin.ModelAdmin):
    list_display = ["word"]
    inlines = [IncorrectInline]

class IncorrectAdmin(admin.ModelAdmin):
    list_display = ["word", "correct"]
admin.site.register(Correct, CorrectAdmin)
admin.site.register(Incorrect, IncorrectAdmin)