from django.contrib import admin
from .models import (MyUser,
                     ToDo)

admin.site.register(MyUser)
admin.site.register(ToDo)
