from django.contrib import admin
from core.models import News, TeamMembers

# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['id','name','photo_main','description','phone_number','email_address','position','hire_date']
    list_display_links = ['id','name','phone_number','email_address']
    search_fields = ['name','phone_number','email_address']
    list_per_page = 10
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','photo_main','description']
    list_display_links = ['title',]
    search_fields = ['title',]
    list_per_page = 10
    
admin.site.register(TeamMembers, TeamMemberAdmin)
admin.site.register(News, NewsAdmin)