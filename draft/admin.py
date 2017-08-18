from django.contrib import admin
# Register your models here.
from filer.admin import FileAdmin
from .models import DraftPlan

admin.site.register(DraftPlan)