from django.contrib import admin
from .models import Question, Result, Profile


admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Profile)
