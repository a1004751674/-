from django.contrib import admin

from .models import Newsdata,frequencycontent,frequencytitle
# Register your models here.

class frequencyAdmin(admin.ModelAdmin):
    list_display = ('word', 'frequency')

class NewsdataAdmin(admin.ModelAdmin):
    list_display = ('title', 'media','time')

admin.site.register(Newsdata,NewsdataAdmin)
admin.site.register(frequencycontent,frequencyAdmin)
admin.site.register(frequencytitle,frequencyAdmin)