from django.contrib import admin
from home.models import login
from home.models import user_data
from home.models import upload
from home.models import reporter

# Register your models here.
admin.site.register(login)
admin.site.register(user_data)
admin.site.register(upload)
admin.site.register(reporter)

