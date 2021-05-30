from django.contrib import admin

# Register your models here.

from .models import Student


class StudentAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'name', 'sex', 'profession',
        'email', 'qq', 'phone', 'status',
        'create_t', 'update_t'
    ]

    list_filter = [
        'sex', 'profession', 'status', 'create_t'
    ]

    search_fields = [
        'name',
        'profession'
    ]

    fieldsets = [
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        })
    ]


admin.site.register(Student, StudentAdmin)
