from django.contrib import admin
from .models import Staff, LineManager



    
admin.site.register(LineManager)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'firstname', 'lastname', 'line_manager_id', 'leave_balance')
    list_filter = ['line_manager_id', 'leave_balance']
