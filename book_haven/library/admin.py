from django.contrib import admin
from .models import TeamMember, Book, FreeBook, PurchaseBook, ContactSubmission

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Book)
admin.site.register(FreeBook)
admin.site.register(PurchaseBook)

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message_display', 'submitted_at')

    def message_display(self, obj):
        # Return a default message if the message field is empty
        return obj.message if obj.message else "No message provided"
    message_display.short_description = 'Message'  # Customize the column name in the admin list

admin.site.register(ContactSubmission, ContactSubmissionAdmin)
