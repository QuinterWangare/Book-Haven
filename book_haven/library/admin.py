from django.contrib import admin
from .models import TeamMember, Book, FreeBook, PurchaseBook

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Book)
admin.site.register(FreeBook)
admin.site.register(PurchaseBook)
