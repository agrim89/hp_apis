import django.forms
from .models import PartnerSalesTeam, Product, Partner, Category


class BaseUserForm(django.forms.ModelForm):

    class Meta:
        model = PartnerSalesTeam
        fields = ['first_name', 'last_name', "email", "username", "dealer_name", "mobile",
                  "address", "gender"]


class CategoryForm(django.forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name',]


class CompanyForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Partner
        fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile",]


class ProductDetailsForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Product
        fields = ['category', 'product', 'part_no', "specification_details", "processor", "screen_size", "warranty",
                  "ram", "hard_disk", "operating_system", "screen", 'odd', 'graphics', "price", "image_url", "status"]
