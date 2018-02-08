import django.forms
from .models import BaseUser, Company, BusinessPC, NoteBook, WorkStation


class BaseUserForm(django.forms.ModelForm):

    class Meta:
        model = BaseUser
        fields = ['first_name', 'last_name', "email", 'password', "username", "dealer_name", "mobile",
                  "address", "gender"]


class CompanyForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = Company
        fields = ['company_name', 'domain_name', "partner_id", 'region', "location", "dedicated_person", "mobile",]


class WorkStationForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = WorkStation
        fields = ['product', 'part_no', "specification_details", "processor", 'graphics', "warranty", "ram",
                  "hard_disk", "odd", "price"]


class BusinessPCForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = BusinessPC
        fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
                  "hard_disk", "operating_system", "screen", "price"]


class NoteBookForm(django.forms.ModelForm):
    """
    User form
    """
    class Meta:
        model = NoteBook
        fields = ['product', 'part_no', "specification_details", "processor", "screen_size", "warranty", "ram",
                  "hard_disk", "operating_system", "screen", "price"]
