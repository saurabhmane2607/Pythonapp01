from django.contrib import admin

# Register your models here.
from Firstapp01.models import Student ,urls
admin.site.register(Student)
admin.site.register(urls)