from django.contrib import admin

# Register your models here.
from .models import total,easy,medium,hard

admin.site.register(total)
admin.site.register(easy)
admin.site.register(medium)
admin.site.register(hard)
