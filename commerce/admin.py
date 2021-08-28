from django.contrib import admin
from commerce import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'ref', 'id')
    readonly_fields = ('search',)


admin.site.register(models.Product, ProductAdmin)
