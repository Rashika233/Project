from django.contrib import admin
from first_app.models import login, training, candidate, Register
# Register your models here.
admin.site.register(login)
admin.site.register(training)
admin.site.register(candidate)
admin.site.register(Register)