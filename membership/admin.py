from django.contrib import admin
from .models import info
admin.site.site_header = 'Shivesena'
admin.site.site_title = "Admin Pannel" 
admin.site.index_title = "Shivsena"
list_per_page = 25
class LocalAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'location', 'email',  'photo_main',)
    search_fields = ['id_number']
admin.site.register(info,LocalAdmin)