from django.db import models
from django.contrib.auth.models import User
import datetime


gender = (
    ("Male", "Male",),
    ("Female", "Female",)
)

category = (
    ('Notebook', 'Notebook'),
    ('BusinessPC', 'BusinessPC' ),
    ('Workstation', 'Workstation')
)


class BaseUser(User):
    dealer_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)
    gender = models.CharField(choices=gender, max_length=10)
    login_count = models.IntegerField()

    def __str__(self):
        return "{} : {}".format(self.username, self.dealer_name)

    def __unicode__(self):
        return "{} : {}".format(self.username, self.dealer_name)

    def save(self, *args, **kwargs):
        if self.last_login:
            self.login_count += 1
        else:
            self.login_count = 0
        super(BaseUser, self).save()


class Company(models.Model):
    company_name = models.CharField(max_length=1000)
    domain_name = models.CharField(max_length=1000)
    partner_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dedicated_person = models.CharField(max_length=100)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{} : {}".format(self.company_name, self.domain_name)

    def __unicode__(self):
        return "{} : {}".format(self.company_name, self.domain_name)


class ProductDetails(models.Model):
    category = models.CharField(max_length=20, choices=category)
    product = models.CharField(max_length=1000)
    part_no = models.CharField(max_length=1000)
    specification_details = models.CharField(max_length=1000)
    processor = models.CharField(max_length=1000)
    screen_size = models.CharField(max_length=1000, null=True, blank=True)
    warranty = models.CharField(max_length=1000)
    ram = models.CharField(max_length=1000)
    hard_disk = models.CharField(max_length=1000)
    operating_system = models.CharField(max_length=1000, null=True, blank=True)
    screen = models.CharField(max_length=1000, null=True, blank=True)
    price = models.CharField(max_length=1000)
    graphics = models.CharField(max_length=1000, null=True, blank=True)
    odd = models.CharField(max_length=1000, null=True, blank=True)
    created = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.created:
            self.modified = now
        else:
            self.modified = now
            self.created = now
        return super(ProductDetails, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} : Rs. {}".format(self.category, self.product, self.price)

    def __unicode__(self):
        return "{} - {} : Rs. {}".format(self.category, self.product, self.price)


# class BusinessPC(models.Model):
#     product = models.CharField(max_length=1000)
#     part_no = models.CharField(max_length=1000)
#     specification_details = models.CharField(max_length=1000)
#     processor = models.CharField(max_length=1000)
#     screen_size = models.CharField(max_length=1000)
#     warranty = models.CharField(max_length=1000)
#     ram = models.CharField(max_length=1000)
#     hard_disk = models.CharField(max_length=1000)
#     operating_system = models.CharField(max_length=1000)
#
#     screen = models.CharField(max_length=1000)
#     price = models.CharField(max_length=1000)
#     created = models.CharField(max_length=100)
#     modified = models.CharField(max_length=100)
#     status = models.BooleanField(default=True)
#
#     def save(self, *args, **kwargs):
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         if self.created:
#             self.modified = now
#         else:
#             self.modified = now
#             self.created = now
#         return super(BusinessPC, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return "{} : Rs. {}".format(self.product, self.price)
#
#     def __unicode__(self):
#         return "{} : {}".format(self.product, self.price)


# class WorkStation(models.Model):
#     product = models.CharField(max_length=1000)
#     part_no = models.CharField(max_length=1000)
#     specification_details = models.CharField(max_length=1000)
#     processor = models.CharField(max_length=1000)
#     warranty = models.CharField(max_length=1000)
#     ram = models.CharField(max_length=1000)
#     hard_disk = models.CharField(max_length=1000)
#     graphics = models.CharField(max_length=1000)
#     odd = models.CharField(max_length=1000)
#     price = models.CharField(max_length=1000)
#     created = models.CharField(max_length=100)
#     modified = models.CharField(max_length=100)
#     status = models.BooleanField(default=True)
#
#     def save(self, *args, **kwargs):
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         if self.created:
#             self.modified = now
#         else:
#             self.modified = now
#             self.created = now
#         return super(WorkStation, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return "{} : Rs. {}".format(self.product, self.price)
#
#     def __unicode__(self):
#         return "{} : Rs. {}".format(self.product, self.price)
