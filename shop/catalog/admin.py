from django.contrib import admin
from .models import Thinners, Im, Ukr_thinners, News, Order, Feedback


class ThinnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "purpose", 'price', 'currency', 'description', 'country', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'country')
    list_filter = ('name', 'price', 'country')


class ImAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
    list_display_links = ('id', 'img')
    search_fields = ('img',)
    list_filter = ('img',)


class UkrthinnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "purpose", 'price', 'currency', 'description', 'country', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'country')
    list_filter = ('name', 'price', 'country')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', "text", 'picture', 'date')
    list_display_links = ('id', 'head')
    search_fields = ('head', 'date')
    list_filter = ('head', 'date')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ukr_name', "purpose", 'description')
    list_display_links = ('id', 'name', 'ukr_name')
    search_fields = ('name', 'ukr_name', 'purpose')
    list_filter = ('name', 'ukr_name', 'purpose')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'mail', 'phone', 'text')
    list_display_links = ('id', 'fio', 'mail')
    search_fields = ('fio', 'mail', 'phone')
    list_filter = ('fio', 'mail', 'phone')


admin.site.register(Thinners, ThinnersAdmin)
admin.site.register(Im, ImAdmin)
admin.site.register(Ukr_thinners, UkrthinnersAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)
