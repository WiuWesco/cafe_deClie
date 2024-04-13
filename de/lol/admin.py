from django.contrib import admin
from .models import *
admin.site.register(vacance)
admin.site.register(MP)
admin.site.register(galary)
admin.site.register(store)
admin.site.register(store_chapter)
admin.site.register(for_main)
@admin.register(feedback)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','sername','email','text')
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request):
        return False
@admin.register(RegMP)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','sername','email','MP')
    def has_add_permission(self, request):
        return False
     # Отключить операцию изменения
    def has_change_permission(self, request):
        return False
@admin.register(reservation)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','sername','number','date','place')
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request):
        return False
admin.site.site_header = 'Управление сайтом'
admin.site.site_title = 'Управление сайтом'
admin.site.index_title = 'Управление сайтом'
