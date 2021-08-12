from ast import parse
from functools import partialmethod
from os import name, truncate
from django.db.models.deletion import CASCADE
from django.utils.regex_helper import contains
from django.utils.translation import activate
from django.db import models
from gymtime import settings
from django.db.models.fields import AutoField, DateField, DateTimeField
from datetime import datetime

# Create your models here.

class Customer01(models.Model):
    CHOICES = (
        ('B', 'Balance Brought Forward'),
        ('P', 'Profit & Loss'),
        ('T', 'Trading'),
    )
    party = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, default=0)
    phone = models.CharField(max_length=100, blank=True, default=0,)
    mobile = models.CharField(max_length=100, blank=True, default=0,)
    mark = models.CharField(
        max_length=100, choices=CHOICES, blank=True, default=0,)
    balbf = models.IntegerField(blank=True, default=0,)
    primaryno = models.AutoField(primary_key=True)
    balance = models.IntegerField(default=0, blank=True)
    opendr = models.IntegerField(default=0, blank=True)
    opencr = models.IntegerField(default=0, blank=True)
    debit = models.IntegerField(default=0, blank=True)
    credit = models.IntegerField(default=0, blank=True)
    closdr = models.IntegerField(default=0, blank=True)
    closcr = models.IntegerField(default=0,  blank=True)

    def __str__(self):
        return self.party


class Cashdet01(models.Model):
    CHOICES = (
        ('BV', 'Bank Voucher'),
        ('CV', 'Cash Voucher'),
        ('JV', 'Journel Voucher'),
    )
    code = models.CharField(max_length=10000)
    salpur = models.CharField(max_length=30, default=0 )
    bill = models.CharField(max_length=30, default=0 )
    party = models.CharField(max_length=30, default=0)
    date = models.DateField(default='2021-01-01')
    partydescript = models.CharField(max_length=30,default=0)
    descript = models.CharField(max_length=100, default=0)
    debit = models.IntegerField(default=0 )
    credit = models.IntegerField(default=0 )
    vouchno = models.CharField(max_length=30 )
    balance = models.IntegerField(default=0 )
    cashbalance = models.IntegerField(default=0 )
    primaryno = models.AutoField(primary_key=True)
    balance1 = models.IntegerField(default=0 )
    vouchtype = models.CharField(max_length=30, choices=CHOICES)
    reconmark = models.CharField(max_length=30, default=0 )
    username = models.CharField(max_length=30 )
    entrydate = models.DateField()
    deleted = models.CharField(max_length=30 )

    def __str__(self):
        return self.vouchno



class Packages(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    charges = models.CharField(
        max_length=100, blank=True, default=0)
    primaryno = models.AutoField(primary_key=True)

    def __str__(self):
        return self.description

class Member(models.Model):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    code = models.CharField(max_length=100, default=0)
    # services = models.ForeignKey(Services, on_delete=models.CASCADE ,default='',null=True)
    name = models.CharField(max_length=100 ,default="Name")
    surname = models.CharField(max_length=100 ,default="Surname")
    gender = models.CharField(max_length=100,blank=True, choices=CHOICES)
    image = models.ImageField(upload_to='member/',
                              default='member/defaultpic.png', blank=True, null=True)
    mobile = models.CharField(max_length=100 ,default=0)
    whatsapp = models.CharField(max_length=100,default=0 )
    dob = models.DateField(default=datetime.now)
    weight = models.FloatField(default=0.0)
    address = models.CharField(max_length=100 ,default=0)
    cnic = models.CharField(max_length=100 ,default=0)
    trainer = models.CharField(max_length=100 ,default=0)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True,blank = True)
    start = models.DateField(default='2021-01-01')
    end = models.DateField(default='2021-01-01')
    notes = models.CharField(max_length=100,default=0 )
    active = models.BooleanField(default=False)
    date = models.DateField(default='2021-01-01')
    trainerfee = models.IntegerField(default=0)
    personaltrainerfee = models.IntegerField(default=0)
    Admissionfee = models.IntegerField(default=0)
    lockerfee = models.IntegerField(default=0)
    lockerno = models.CharField(max_length=100, default=0)
    totalfee = models.IntegerField( default=0)
    primaryno = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

# class Member_charges(models.Model):
#     memberid = models.CharField(max_length=100)





class Packages_S(models.Model):
    package = models.CharField(max_length=100 )
    service = models.CharField(max_length=100 )
    primaryno = models.AutoField(primary_key=True)

    def __str__(self):
        return self.package




class Trainee(models.Model):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    code = models.CharField(max_length=100, default=0)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True, choices=CHOICES)
    cnic = models.CharField(max_length=100, blank=True, default=0)
    contact = models.CharField(max_length=100, blank=True, default=0)
    dob = models.DateField(blank=True, null=True,default='2021-01-01')
    image = models.ImageField(upload_to='trainee/',
                              default='trainee/defaultpic.png', blank=True, null=True)
    primaryno = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    CHOICES_ = (
        ('01', 'Janurary'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )
    CHOICES = (
        ('2021', '2021'),
        ('2022', '2022')
    )
    CHOICES__ = (
        ('Due', 'Due'),
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid')
    )
    trans_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=4,choices=CHOICES)
    month = models.CharField(max_length=2,choices=CHOICES_)
    member_code = models.ForeignKey(Member,on_delete=CASCADE,default="0")
    due_amt = models.IntegerField(default=0)
    due_date = models.DateField(default='2021-01-01')
    paid_amt = models.IntegerField(default=0)
    paid_date = models.DateField(default='2021-01-01')
    balance = models.IntegerField(default=0)
    vouchno = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=10,choices= CHOICES__)
    def __str__(self):
        return self.vouchno
