from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .forms import BaseUserForm, CompanyForm, ProductDetailsForm, CategoryForm
from .models import PartnerSalesTeam, Product, Partner, Category


class BaseUserAdmin(admin.ModelAdmin):
    form = BaseUserForm
    fields = [('first_name', 'last_name'), ("email", "username"), "password", "dealer_name", "mobile",
              "address", "gender", "is_active"]
    list_display = ('first_name', 'mobile', 'email', 'dealer_name', 'last_login', 'login_count','is_active')
    list_filter = ('is_active',)
    search_fields = ['email', 'mobile']


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    fields = ["name", 'status']
    list_display = ("name", 'status')
    search_fields = ['name']


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile", ]
    list_display = ('company_name', 'domain_name', "partner_id", "location")
    list_filter = ('status',)
    search_fields = ['company_name', "partner_id"]


class ProductDetailsAdmin(admin.ModelAdmin):
    form = ProductDetailsForm
    fields = ['category','product', 'part_no', "specification_details", "processor", "screen_size", "warranty",
              "ram", "hard_disk", "operating_system", "screen",'odd', 'graphics', "price", "data_sheet", "image_url",
              "status"]

    list_display = ('category', 'product', "processor", "hard_disk", "ram", 'price', "modified")
    list_filter = ('category', 'ram', "processor", "hard_disk")
    search_fields = ['product']


class HewlettPackardAdminSite(AdminSite):
    site_title = ugettext_lazy('Hewlett-Packard Admin')

    site_header = ugettext_lazy('HP Admin')

    index_title = ugettext_lazy('Dashboard')


admin_site = HewlettPackardAdminSite()


admin_site.register(PartnerSalesTeam, BaseUserAdmin)
admin_site.register(Partner, CompanyAdmin)
admin_site.register(Product, ProductDetailsAdmin)
admin_site.register(Category, CategoryAdmin)
# admin_site.register(NoteBook, NoteBookAdmin)
# admin_site.register(WorkStation, WorkStationAdmin)
