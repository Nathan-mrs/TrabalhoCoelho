from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import aluno, frequencia

admin.site.register(aluno)
admin.site.register(frequencia)
