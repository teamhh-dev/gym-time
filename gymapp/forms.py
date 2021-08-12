from django.db import models
from django.db.models import fields
from django import forms
from django.forms import ModelForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class Chartsofaccounts(ModelForm):
    class Meta:
        model = Customer01
        fields = ['party','description','phone','mobile','balbf','address','mark']


class Packages_f(ModelForm):
    class Meta:
        model = Packages
        fields = ['description', 'charges']


class Trainee_f(ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'gender', 'cnic','dob' ,'contact','image',]


class Member_f(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        exclude = ('code', 'trainer','dob', )

 
class Cashdet01_f(ModelForm):
    class Meta:
        model = Cashdet01
        fields = "__all__"
        exclude = ('salpur', 'bill', 'reconmark',
                   'username', 'deleted', 'vouchno','code', 'date')

class Transaction_f(ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"