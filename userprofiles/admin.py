# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import UserProfile
from actions import export_as_excel


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grupo', 'slug', 'image_avatar_admin', 'es_staff', )
    list_filter = ('user', 'grupo', )
    search_fields = ('grupo', 'slug',)
    list_editable = ('grupo', 'slug', )
    actions = (export_as_excel, )
    raw_id_fields = ('user', )

    def es_staff(self, obj):
        return obj.user.is_staff == 1

    es_staff.boolean = True

    """
    def imagenavataradmin(self, obj):
        url = obj.image_avatar_admin()
        tag = '<img src="%s">' % url
        return tag
    """


# admin.site.register(UserProfile, UserProfileAdmin)
