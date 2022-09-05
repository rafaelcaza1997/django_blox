
from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','body_content','description','category_id','publi','date_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('tech','usecase','description')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)