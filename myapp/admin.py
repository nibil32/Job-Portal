from django.contrib import admin

# Register your models here.
from myapp.models import job,category,student
admin.site.register(category)
admin.site.register(job)
admin.site.register(student)