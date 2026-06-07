from django.contrib import admin
from .models import *


admin.site.register(Hero)
admin.site.register(History)
# admin.site.register(Gallery)
admin.site.register(VideoGallery)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(About_Hill)
admin.site.register(About_Temple)
admin.site.register(About_Culture)
admin.site.register(About_mission)
admin.site.register(Santhal_jain)


# history_________________________________________________________
class HistoryImageInline(admin.TabularInline):
    model = HistoryImage


class MainHistoryAdmin(admin.ModelAdmin):
    inlines = [HistoryImageInline]


admin.site.register(Main_History, MainHistoryAdmin)


# history_________________________________________________________
admin.site.register(Religen)

admin.site.register(Judicial)

admin.site.register(Main_docoment)

admin.site.register(Contect)

class AboutImagesInline(admin.TabularInline):
    model = AboutImages
    extra = 4


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [AboutImagesInline]







# Gelllery folder________________________________________________________________________________________________________________
@admin.register(All_Gellery)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")

@admin.register(All_Video)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video")












