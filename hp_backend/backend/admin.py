from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .forms import BaseUserForm, CompanyForm, NoteBookForm, WorkStationForm, BusinessPCForm
from .models import BaseUser, Company, NoteBook, WorkStation, BusinessPC


class BaseUserAdmin(admin.ModelAdmin):
    form = BaseUserForm
    fields = [('first_name', 'last_name'), ("email", "username"),'password', "dealer_name", "mobile",
              "address", "gender", "is_active"]
    list_display = ('username', 'is_active',)
    list_filter = ('is_active',)


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile", ]
    list_display = ('company_name', 'domain_name',)
    list_filter = ('status',)


class WorkStationAdmin(admin.ModelAdmin):
    form = WorkStationForm
    fields = ['product', 'part_no', "specification_details", "processor", 'graphics', "warranty", "ram",
              "hard_disk", "odd", "price"]
    list_display = ('product', "processor", "hard_disk", "ram", 'price', "modified")
    list_filter = ('ram', "processor", "hard_disk")


class BusinessPCAdmin(admin.ModelAdmin):
    form = BusinessPCForm
    fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
              "hard_disk", "operating_system", "screen", "price"]
    list_display = ('product', "processor", "screen_size", "ram", 'price', "modified")
    list_filter = ('ram', "processor", "hard_disk")


class NoteBookAdmin(admin.ModelAdmin):
    form = NoteBookForm
    fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
              "hard_disk", "operating_system", "screen", "price"]
    list_display = ('product', "processor", "screen_size", "ram", 'price', "modified")
    list_filter = ('ram', "processor", "hard_disk")


class HewlettPackardAdminSite(AdminSite):
    site_title = ugettext_lazy('Hewlett-Packard Admin')

    site_header = ugettext_lazy('HP Admin')

    index_title = ugettext_lazy('HP Admin')


admin_site = HewlettPackardAdminSite()


admin_site.register(BaseUser, BaseUserAdmin)
admin_site.register(Company, CompanyAdmin)
admin_site.register(BusinessPC, BusinessPCAdmin)
admin_site.register(NoteBook, NoteBookAdmin)
admin_site.register(WorkStation, WorkStationAdmin)
