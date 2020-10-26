# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'categories'


class CompanyInformation(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    password = models.TextField()
    name = models.CharField(max_length=256)
    name_kana = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=16)
    mail_address = models.CharField(max_length=255)
    address = models.CharField(max_length=256)
    address_kana = models.CharField(max_length=512, blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    logo_image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_information'
        unique_together = (('id', 'mail_address'),)


class ItemInformation(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=256)
    price = models.BigIntegerField()
    tax_id = models.IntegerField()
    information = models.TextField(blank=True, null=True)
    stock = models.IntegerField()
    categories_one = models.IntegerField(blank=True, null=True)
    categories_two = models.IntegerField(blank=True, null=True)
    categories_three = models.IntegerField(blank=True, null=True)
    created_company_id = models.CharField(max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_information'


class ItemsReview(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    item_id = models.CharField(max_length=36)
    review = models.FloatField()
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'items_review'


class PurchaseHistory(models.Model):
    user_id = models.CharField(max_length=36)
    item_id = models.CharField(max_length=36)
    item_count = models.IntegerField()
    purchased_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'purchase_history'


class ShoppingCart(models.Model):
    user_id = models.CharField(max_length=36)
    item_id = models.CharField(max_length=36)
    item_count = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shopping_cart'


class SystemAdminInformation(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    password = models.TextField()
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_admin_information'


class Tax(models.Model):
    id = models.IntegerField(primary_key=True)
    tax = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tax'


class UserInformation(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    password = models.TextField()
    name = models.CharField(max_length=256)
    name_kana = models.CharField(max_length=512)
    mail_address = models.CharField(max_length=255)
    address = models.CharField(max_length=256)
    address_kana = models.CharField(max_length=512, blank=True, null=True)
    zip_code = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_information'
        unique_together = (('id', 'mail_address'),)
