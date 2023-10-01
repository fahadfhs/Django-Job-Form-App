from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")  # lets you display the details in the admin page
    search_fields = ("first_name", "last_name", "email")  # shows the search field
    list_filter = ("date", "occupation")  # helps you filter data
    ordering = ("-first_name",)  # shows the name in ordered or descending in -
    readonly_fields = ("occupation",)


admin.site.register(Form, FormAdmin)
