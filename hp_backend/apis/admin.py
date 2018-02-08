from django.contrib import admin
from .models import BaseUser, Company, NoteBook, WorkStation, BusinessPC
from .forms import BaseUserForm, CompanyForm, NoteBookForm, WorkStationForm, BusinessPCForm
from django.contrib.auth.models import User,Group

class BaseUserAdmin(admin.ModelAdmin):
    form = BaseUserForm
    fields = [('first_name', 'last_name'), ("email", "username"),'password', "dealer_name", "mobile",
              "address", "gender"]


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile", ]


class WorkStationAdmin(admin.ModelAdmin):
    form = WorkStationForm
    fields = ['product', 'part_no', "specification_details", "processor",'graphics', "warranty", "ram",
              "hard_disk", "odd", "price"]


class BusinessPCAdmin(admin.ModelAdmin):
    form = BusinessPCForm
    fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
              "hard_disk", "operating_system", "screen", "price"]


class NoteBookAdmin(admin.ModelAdmin):
    form = NoteBookForm
    fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
              "hard_disk", "operating_system", "screen", "price"]

admin.site.site_header='HP Administration'
admin.site.site_title='HP Admin'

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(BusinessPC, BusinessPCAdmin)
admin.site.register(NoteBook, NoteBookAdmin)
admin.site.register(WorkStation, WorkStationAdmin)
