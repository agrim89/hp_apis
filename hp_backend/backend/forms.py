import django.forms
from .models import BaseUser, Company, ProductDetails


class BaseUserForm(django.forms.ModelForm):

    class Meta:
        model = BaseUser
        fields = ['first_name', 'last_name', "email", "username", "dealer_name", "mobile",
                  "address", "gender"]


class CompanyForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Company
        fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile",]


class ProductDetailsForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = ProductDetails
        fields = ['category', 'product', 'part_no', "specification_details", "processor", "screen_size", "warranty",
                  "ram", "hard_disk", "operating_system", "screen", 'odd', 'graphics', "price", "image_url", "status"]
#
# class BusinessPCForm(django.forms.ModelForm):
#     """
#     User form
#     """
#     class Meta:
#         model = BusinessPC
#         fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
#                   "hard_disk", "operating_system", "screen", "price"]
#
#
# class NoteBookForm(django.forms.ModelForm):
#     """
#     User form
#     """
#     class Meta:
#         model = NoteBook
#         fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
#                   "hard_disk", "operating_system", "screen", "price"]
