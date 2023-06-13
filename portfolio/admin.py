from django.contrib import admin
from portfolio.models import Contact,Blog,Internship
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)


class InternshipAdmin(admin.ModelAdmin):
    list_display=(
        'fullname',
    'usn',
    'email', 
    'college_name', 
    'offer_status', 
    'start_date', 
    'end_date', 
    'proj_report', 
    'timeStamp'
    )
    search_fields=('fullname', 'usn', 'email')
    list_filter =['college_name', 'proj_report', 'offer_status',  ]
admin.site.register(Internship, InternshipAdmin)