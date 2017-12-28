from django.contrib import admin
from .models import Circuit, CirctuiDetail, ImageUpload, lesinfos, Prisencharche, HomeDetail, Mots

# Register your models here.

admin.site.register(Circuit)
admin.site.register(CirctuiDetail)
admin.site.register(ImageUpload)
admin.site.register(lesinfos)
admin.site.register(HomeDetail)
admin.site.register(Mots)

