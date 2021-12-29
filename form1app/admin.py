from django.contrib import admin
from form1app.models import studentdetails
# Register your models here.

class studentdetailsAdmin(admin.ModelAdmin):

	list_display = ('usn','name','age','gender','course')

admin.site.register(studentdetails,studentdetailsAdmin)
