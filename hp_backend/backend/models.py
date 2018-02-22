from django.db import models
from django.contrib.auth.models import User
import datetime


gender = (
    ("Male", "Male",),
    ("Female", "Female",)
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.CharField(max_length=100, null=True, blank=True)
    modified = models.CharField(max_length=100, null=True, blank=True)
    status = models.NullBooleanField(default=True)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.created:
            self.modified = now
        else:
            self.modified = now
            self.created = now
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Category"

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return "{}".format(self.name)


class Partner(models.Model):
    company_name = models.CharField(max_length=1000)
    domain_name = models.CharField(max_length=1000)
    partner_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dedicated_person = models.CharField(max_length=100)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-company_name']
        verbose_name_plural = "Partner"

    def __str__(self):
        return "{}".format(self.company_name)

    def __unicode__(self):
        return "{}".format(self.company_name)


class PartnerSalesTeam(User):
    dealer_name = models.ForeignKey(to=Partner, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)
    gender = models.CharField(choices=gender, max_length=10)
    login_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('email',)
        verbose_name_plural = "PartnerSalesTeam"

    def __str__(self):
        return "{} : {}".format(self.username, self.dealer_name.company_name)

    def __unicode__(self):
        return "{} : {}".format(self.username, self.dealer_name.company_name)


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
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
    price = models.IntegerField()
    graphics = models.CharField(max_length=1000, null=True, blank=True)
    odd = models.CharField(max_length=1000, null=True, blank=True)
    created = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1000)
    data_sheet = models.URLField(max_length=1000)

    class Meta:
        ordering = ('product',)
        verbose_name_plural = "Product"

    def save(self, *args, **kwargs):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.created:
            self.modified = now
        else:
            self.modified = now
            self.created = now
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} : Rs. {}".format(self.category, self.product, self.price)

    def __unicode__(self):
        return "{} - {} : Rs. {}".format(self.category, self.product, self.price)
