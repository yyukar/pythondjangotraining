from django.contrib import admin
from .models import ipsumuye
from .models import ipsumuyebilgi
from .models import ipsumuyetip
from .models import ipsumuyeodeme

class ipsumuyeAdmin(admin.ModelAdmin):
  list_display = ("uyeNo", "ad", "soyad","seviye",)
  
# Register your models here.
admin.site.register(ipsumuye,ipsumuyeAdmin)
admin.site.register(ipsumuyebilgi)
admin.site.register(ipsumuyetip)
admin.site.register(ipsumuyeodeme)
