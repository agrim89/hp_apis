import django.forms
from .models import PartnerSalesTeam, Product, Partner, Category, UserType, ProductType


class BaseUserForm(django.forms.ModelForm):

    class Meta:
        model = PartnerSalesTeam
        fields = ['first_name', 'last_name', "email", "username", "dealer_name", "mobile",
                  "address", "gender"]


class CategoryForm(django.forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name',]


class UserTypeForm(django.forms.ModelForm):

    class Meta:
        model = UserType
        fields = ['name',]


class ProductTypeForm(django.forms.ModelForm):

    class Meta:
        model = ProductType
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
    # """

    class Meta:
        model = Product
        fields = ['category', 'product', "user_type", "product_type", 'part_no', "specification_details", "processor",
                  "screen_size", "warranty", "ram", "hard_disk", "operating_system", "screen", 'odd', 'graphics',
                  "price", "image_url", "status"]

        widgets = {
            "user_type": django.forms.SelectMultiple(attrs={'cols': 1, "rows": 10}),
            "product_type": django.forms.SelectMultiple(attrs={'cols': 1, "rows": 10}),
        }