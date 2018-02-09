from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .forms import BaseUserForm, CompanyForm, NoteBookForm, WorkStationForm, BusinessPCForm
from .models import BaseUser, Company, NoteBook, WorkStation, BusinessPC


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


class HewlettPackardAdminSite(AdminSite):
    site_title = ugettext_lazy('Hewlett-Packard Admin')

    site_header = ugettext_lazy('Hewlett-Packard administration')

    index_title = ugettext_lazy('Hewlett-Packard administration')


admin_site = HewlettPackardAdminSite()

# admin_site.site_header='HP Administration'
# admin_site.site_title='HP Admin'


admin_site.register(BaseUser, BaseUserAdmin)
admin_site.register(Company, CompanyAdmin)
admin_site.register(BusinessPC, BusinessPCAdmin)
admin_site.register(NoteBook, NoteBookAdmin)
admin_site.register(WorkStation, WorkStationAdmin)
