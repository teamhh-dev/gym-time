from django.contrib.admin.sites import all_sites
from .models import *
from django.contrib import admin
# Register your models here.

#admin.site.register(Cashdet, Cashdet01, Charge_sheet,Comid,Customer,Customer01,Formnames,Inquiry,Member,Packages,Packages_S,Services,Trainee)

admin.site.register(Cashdet01)
admin.site.register(Customer01)
admin.site.register(Packages)
admin.site.register(Packages_S)
admin.site.register(Trainee)
admin.site.register(Member)
admin.site.register(Transactions)

