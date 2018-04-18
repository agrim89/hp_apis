from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .forms import BaseUserForm, CompanyForm, ProductDetailsForm, CategoryForm, UserTypeForm, ProductTypeForm
from .models import PartnerSalesTeam, Product, Partner, Category, UserType, ProductType
from django.db.models import Count, Sum


class BaseUserAdmin(admin.ModelAdmin):
    form = BaseUserForm
    fields = [('first_name', 'last_name'), ("email", "username"), "password", "dealer_name", "mobile",
              "address", "gender", "is_active"]
    list_display = ('first_name', 'mobile', 'email', 'dealer_name', 'last_login', 'login_count','is_active')
    list_filter = ('is_active',)
    search_fields = ['email', 'mobile']


class UserTypeAdmin(admin.ModelAdmin):
    form = UserTypeForm
    fields = ["name",]
    list_display = ("name",)
    search_fields = ['name']


class ProductTypeAdmin(admin.ModelAdmin):
    form = ProductTypeForm
    fields = ["name",]
    list_display = ("name",)
    search_fields = ['name']


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
    fields = [('product', 'category'), 'description', ("user_type", "product_type"), ('part_no', "specification_details"),
              ("processor", "screen_size"), ("warranty", "ram"), ("hard_disk", "operating_system"), ("screen", 'odd'),
              ('graphics', "price"), "data_sheet", "image_url", "status"]

    list_display = ('category', 'product', "processor", "hard_disk", "ram", 'price', "modified")
    list_filter = ('category', 'ram', "processor", "hard_disk", "user_type", "product_type")
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
admin_site.register(UserType, UserTypeAdmin)
admin_site.register(ProductType, ProductTypeAdmin)
# admin_site.register(NoteBook, NoteBookAdmin)
# admin_site.register(WorkStation, WorkStationAdmin)
