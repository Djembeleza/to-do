from django.contrib import admin
from .models import (MyUser,
                     ToDo)
# from django.contrib.auth.admin import (UserAdmin)

admin.site.register(MyUser)
admin.site.register(ToDo)
