from django.contrib import admin

from .models import Backend, Frontend, DataScience, Register

admin.site.register(Backend)
admin.site.register(Frontend)
admin.site.register(DataScience)
admin.site.register(Register)
