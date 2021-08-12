from typing import List
from django.db.models.query import EmptyQuerySet, InstanceCheckMeta
from django.forms.widgets import DateTimeInput
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import User
from django.views.generic import ListView
import json
from django.template.loader import render_to_string
from django.db.models import Sum
from datetime import datetime
#from weasyprint import HTML
import tempfile


# Create your views here.
@unauthenticated_user
def loginpage(request):
    # print(Group.objects.all())
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/dashboard/')
        else:
            messages.info(request,'Username or Password is Incorrect ')
    context = {}
    return render(request,'gymtime/login.html',context)


@login_required(login_url='login')
def Logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def changepassword(request):
    # userr = User.objects.get(request.POST, id=pk)
    userr = User.objects.get(username=request.user)
    context = {}
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if request.method == "POST":
        if(password1==password2):
            userr.set_password(password1)
            userr.save()
 
        return redirect('/dashboard/', context)
    return render(request, 'gymtime/changepassword.html', context)


@login_required(login_url='login')
def dashboard(request):
    members = Member.objects.filter(active=True).count()
    dues = Transactions.objects.filter(
        due_date=datetime.today().strftime('%Y-%m-%d'), status="Due").aggregate(Sum('due_amt'))
    dues_detail = Transactions.objects.filter(
        due_date=datetime.today().strftime('%Y-%m-%d'), status="Due")
    members_notactive = Member.objects.filter(active=False).count()
    dues = dues['due_amt__sum']
    #print("duess :", )

    context = {'members': members, 'dues': dues,
               'dues_detail': dues_detail, 'members_notactive': members_notactive}
    return render(request,'gymtime/dashboard.html',context)

   

@login_required(login_url='login')
def chartofaccounts(request):
    # print(Cashdet01.objects.values_list('party'))

    form = Chartsofaccounts()
    customer01 = Customer01.objects.all()
    context = {'form':form,'customer01':customer01}
    if 'save' in request.POST :
        form = Chartsofaccounts(request.POST)
        # form.instance.mark = 
        if form.is_valid():
            form.save()
            return redirect('/chartofaccounts/', context)
            
    return render(request,'gymtime/ChartsOfAccount.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatechartofaccounts(request,pk):
    customer01 = Customer01.objects.get(primaryno=pk)
    form = Chartsofaccounts(instance=customer01)
    customer02 = Customer01.objects.all()
    context = {'form': form, 'customer01': customer02}
    if 'save' in request.POST:
        form = Chartsofaccounts(request.POST,instance=customer01)
        if form.is_valid():
            form.save()
            return redirect('/chartofaccounts/', context)

    return render(request, 'gymtime/ChartsOfAccount.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletechartofaccounts(request, pk):
    customer01 = Customer01.objects.get(primaryno=pk)
    context = { 'customer01': customer01}
    if 'delete' in request.POST:
        customer01.delete()
        return redirect('/chartofaccounts/', context)
    elif 'cancel' in request.POST:
        return redirect('/chartofaccounts/', context)

    return render(request, 'gymtime/ChartsOfAccount_confirmdelete.html', context)


@login_required(login_url='login')
def trainee(request):
    form = Trainee_f()
    trainies = Trainee.objects.all()
    context = {'form': form, 'trainies': trainies}
    num = [0]
    for e in trainies:
        num.append(int(e.code))
    code = int(max(num))

    if 'save' in request.POST:
        #form.name = request.POST['dob']
        form = Trainee_f(request.POST, request.FILES)
        if form.is_valid():
            if(code <= 8):
                code = "0"+str(code+1)
            elif(code >= 9):
                code = str(code+1)
            TraineData = Trainee(
                code=code,
                name=form.cleaned_data.get('name'),
                gender=form.cleaned_data.get('gender'),
                cnic=form.cleaned_data.get('cnic'),
                contact=form.cleaned_data.get('contact'),
                dob=form.cleaned_data.get('dob'),
                image=form.cleaned_data.get('image'))
            TraineData.save()
            return redirect('/traniee/', context)

    return render(request, 'gymtime/trainee.html', context)


@login_required(login_url='login')
def packages(request):
    context = {}
    form = Packages_f()
    packages = Packages.objects.all()
    context = {'form': form, 'packages': packages}
    num = [0]
    for e in packages:
        num.append(int(e.code))
    code = int(max(num))
    if 'save' in request.POST:
        form = Packages_f(request.POST)
        if form.is_valid():
            if(code <= 8):
                code = "0"+str(code+1)
            elif(code >= 9):
                code = str(code+1)
            Packagesdata = Packages(code=code, description=form.cleaned_data.get('description'), charges=form.cleaned_data.get('charges'))
            Packagesdata.save()
            return redirect('/packages/', context)
    return render(request, 'gymtime/packages.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatepackages(request, pk):
    package = Packages.objects.get(primaryno=pk)
    form = Packages_f(instance=package)
    packages = Packages.objects.all()
    context = {'form': form, 'packages': packages, 'package': package}
    if 'save' in request.POST:
        form = Packages_f(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('/packages/', context)
    if 'cancel' in request.POST:
        return redirect('/packages/')

    return render(request, 'gymtime/packages_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletepackage(request, pk):
    package = Packages.objects.get(primaryno=pk)
    context = {'package': package}
    if 'delete' in request.POST:
        package.delete()
        return redirect('/packages/', context)
    elif 'cancel' in request.POST:
        return redirect('/packages/', context)

    return render(request, 'gymtime/packages_confirmdelete.html', context)


@login_required(login_url='login')
def code(model):
    model = model.objects.all()
    num = []
    for e in model:
        num.append(int(e.model))
    return int(max(num))



@login_required(login_url='login')
def members(request):
    form = Member_f()
    members = Member.objects.all()
    context = {'form': form, 'members': members}
    num = [0]
    for e in members:
        num.append(int(e.code))
    code = int(max(num))

    if 'save' in request.POST:
        #form.name = request.POST['dob']
        form = Member_f(request.POST, request.FILES)
        if form.is_valid():
            if(code <= 8):
                code = "0"+str(code+1)
            elif(code >= 9):
                code = str(code+1)
            MemberData = Member(
                code=code, 
                name=form.cleaned_data.get('name'), 
                surname=form.cleaned_data.get('surname'),
                gender=form.cleaned_data.get('gender'), 
                image=form.cleaned_data.get('image'),
                mobile=form.cleaned_data.get('mobile'),
                whatsapp=form.cleaned_data.get('whatsapp'),
                weight=form.cleaned_data.get('weight'),
                address=form.cleaned_data.get('address'),
                cnic=form.cleaned_data.get('cnic'),
                package=form.cleaned_data.get('package'),
                start=form.cleaned_data.get('start'),
                end=form.cleaned_data.get('end'),
                active=form.cleaned_data.get('active'),
                trainerfee=form.cleaned_data.get('trainerfee'),
                personaltrainerfee=form.cleaned_data.get('personaltrainerfee'),
                Admissionfee=form.cleaned_data.get('Admissionfee'),
                lockerfee=form.cleaned_data.get('lockerfee'),
                lockerno=form.cleaned_data.get('lockerno'),
                totalfee=form.cleaned_data.get('totalfee'),
                notes=form.cleaned_data.get('notes'),
                date=form.cleaned_data.get('date'),
                )
            MemberData.save()
            if form.cleaned_data.get('Admissionfee') !=0:
                voucherss = Cashdet01.objects.filter(
                    vouchtype='JV', entrydate=form.cleaned_data.get('date'))
                num = [0]
                for e in voucherss:
                    num.append(int(e.code))
                code = int(max(num))
                if(code <= 8):
                    code = "00"+str(code+1)
                elif(code >= 99):
                    code = "0"+str(code+1)
                elif(code >= 100):
                    code = str(code+1)

                vocherno = 'JV'+(str(form.cleaned_data.get('date')).replace('-', ''))
                vocherno = vocherno + code
                Cashdet01Data = Cashdet01(
                    code=code,
                    salpur="salpur",
                    bill="bill",
                    party="090001",
                    partydescript="Cash",
                    descript="Admission Fee--"+code+"-"+form.cleaned_data.get('name'),
                    debit=form.cleaned_data.get('Admissionfee'),
                    credit=0,  
                    vouchno=vocherno,
                    balance=0,
                    cashbalance=0,
                    balance1=0,
                    vouchtype='JV',
                    reconmark="0",
                    username=request.user,
                    entrydate=form.cleaned_data.get('date'),
                    deleted='0'
                )
                Cashdet01Data.save()
                return redirect('/members/', context)
            return redirect('/members/', context)

    return render(request, 'gymtime/members.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatemember(request, pk):
    member = Member.objects.get(primaryno=pk)
    form = Member_f(instance=member)
    members = Member.objects.all()
    obj = 0
    if(member.image == " "):
        obj = None
    context = {'form': form, 'members': members,
               'member': member, "check": obj}
    if 'save' in request.POST:
        form = Member_f(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/members/', context)
    if 'cancel' in request.POST:
        return redirect('/members/')
    return render(request, 'gymtime/members_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletemembers(request, pk):
    member = Member.objects.get(primaryno=pk)
    context = {'member': member}
    if 'delete' in request.POST:
        member.delete()
        return redirect('/members/')
    elif 'cancel' in request.POST:
        return redirect('/members/')

    return render(request, 'gymtime/members_deleteconfirmation.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatetrainee(request, pk):
    trainie = Trainee.objects.get(primaryno=pk)
    form = Trainee_f(instance=trainie)
    trainies = Trainee.objects.all()
    obj = 0
    if(trainie.image==" "):
        obj = None
    context = {'form': form, 'trainies': trainies, 'trainie': trainie,"check":obj}
    if 'save' in request.POST:
        form = Trainee_f(request.POST, request.FILES, instance=trainie)
        if form.is_valid():
            form.save()
            return redirect('/traniee/', context)
    if 'cancel' in request.POST:
        return redirect('/traniee/')
    return render(request, 'gymtime/trainee_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletetrainee(request, pk):
    trainie = Trainee.objects.get(primaryno=pk)
    context = {'trainie': trainie}
    if 'delete' in request.POST:
        trainie.delete()
        return redirect('/traniee/', context)
    elif 'cancel' in request.POST:
        return redirect('/traniee/', context)

    return render(request, 'gymtime/trainee_deleteconfim.html', context)


@login_required(login_url='login')
def accountsvouchers(request):
    form = Cashdet01_f()
    vouchers = Cashdet01.objects.all()
    chartsofaccounts = Customer01.objects.all()
    # json.dumps(accounts)
    data_check = True
    context = {'vouchers': vouchers, 'form': form,
               'chartsofaccounts': chartsofaccounts, 'data_check': data_check}
    if 'submit' in request.POST and request.POST.get('voucher') == 'new' and Customer01.objects.filter(party=request.POST.get('party')):
        print("in the new request")
        form = Cashdet01_f(request.POST)
        if form.is_valid():
            partyt = form.cleaned_data.get('party')
            #partyincoa = Customer01.objects.get(party=partyt)
            #print(partyt,"   in the form   ",partyincoa)
            if form.cleaned_data.get('vouchtype') == "BV" :
                voucherss = Cashdet01.objects.filter(
                    vouchtype='BV', entrydate=form.cleaned_data.get('entrydate'))
            elif form.cleaned_data.get('vouchtype') == "CV":
                voucherss = Cashdet01.objects.filter(
                    vouchtype='CV', entrydate=form.cleaned_data.get('entrydate'))
            elif form.cleaned_data.get('vouchtype') == "JV":
                voucherss = Cashdet01.objects.filter(
                    vouchtype='JV', entrydate=form.cleaned_data.get('entrydate'))

            num = [0]
            for e in voucherss:
                num.append(int(e.code))
            code = int(max(num))
            if(code <= 8):
                code = "00"+str(code+1)
            elif(code <= 99):
                code = "0"+str(code+1)
            elif(code >= 100):
                code = str(code+1)
            
            
            vocherno = form.cleaned_data.get(
                'vouchtype')+(str(form.cleaned_data.get('entrydate')).replace('-', ''))
            vocherno = vocherno + code
            balancee = Cashdet01.objects.filter(
                vouchno=vocherno).aggregate(Sum('credit'))
            
            print("Credit : ",form.cleaned_data.get('credit'))
            form.balance = balancee
            Cashdet01Data = Cashdet01(
                code = code,
                salpur="salpur",
                bill="bill",
                date=form.cleaned_data.get('entrydate'),
                party=form.cleaned_data.get('party'),
                partydescript=form.cleaned_data.get('partydescript'),
                descript=form.cleaned_data.get('descript'),
                debit=form.cleaned_data.get('debit'),
                credit=form.cleaned_data.get('credit'),
                vouchno=vocherno,
                balance=form.cleaned_data.get('balance'),
                cashbalance=form.cleaned_data.get('cashbalance'),
                balance1=form.cleaned_data.get('balance1'),
                vouchtype=form.cleaned_data.get('vouchtype'),
                reconmark= "0",
                username=request.user,
                entrydate=form.cleaned_data.get('entrydate'),
                deleted = '0'
            )
            Cashdet01Data.save()
            return redirect('/vouchers/')
    if 'cancel' in request.POST:
        return redirect('/vouchers/')
    if 'submit' in request.POST and request.POST.get('voucher') == 'old' and request.POST.get('Voucherno') != None:
        context = {}
        voucherss = Cashdet01.objects.filter(
            vouchno=request.POST.get('Voucherno'))
        data_check = True
        vouchno_h=request.POST.get('Voucherno')
        vouchertype = vouchno_h[:2]
        dateyyyy = vouchno_h[2:6]
        datemm = vouchno_h[6:8]
        datedd = vouchno_h[8:10]
        date = dateyyyy+"-"+datemm+"-"+datedd
        code = vouchno_h[10:13]
        print(request.POST.get('debit'))
        if Customer01.objects.filter(party=request.POST.get('party')):
            Cashdet01Data = Cashdet01(
                code=code,
                salpur="salpur",
                bill="bill",
                date=form.cleaned_data.get('entrydate'),
                party=request.POST.get('party'),
                partydescript=request.POST.get('partydescript'),
                descript=request.POST.get('descript'),
                debit=request.POST.get('debit'),
                credit=request.POST.get('credit'),
                vouchno=vouchno_h,
                balance=request.POST.get('balance'),
                cashbalance=request.POST.get('cashbalance'),
                balance1=request.POST.get('balance1'),
                vouchtype=vouchertype,
                reconmark="0",
                username=request.user,
                entrydate=date,
                deleted='0'
            )
            Cashdet01Data.save()
            context = {'vouchers': voucherss, 'form': form, 'dateold': date, 'vouchertype': vouchertype,
                       'chartsofaccounts': chartsofaccounts, 'data_check': data_check, }
            
            return render(request, 'gymtime/voucher_old.html', context)
        else:
            #return redirect('/voucher/')
            context = {'vouchers': voucherss, 'form': form,'dateold': date, 'vouchertype': vouchertype,
                    'chartsofaccounts': chartsofaccounts,'data_check': data_check, }
            
            return render(request, 'gymtime/voucher_old.html', context)
    return render(request, 'gymtime/voucher.html', context)


@login_required(login_url='login')
def oldaccountsvouchers(request):
    form = Cashdet01_f()
    vouchers = Cashdet01.objects.all()
    chartsofaccounts = Customer01.objects.all()
    # json.dumps(accounts)
    context = {'vouchers': vouchers, 'form': form,
               'chartsofaccounts': chartsofaccounts, }
    return render(request, 'gymtime/voucher_old.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteaccountsvouchers(request, pk):
    accountvoucher = Cashdet01.objects.get(primaryno=pk)
    context = {'voucher': accountvoucher}
    if 'delete' in request.POST:
        accountvoucher.delete()
        return redirect('/vouchers/')
    elif 'cancel' in request.POST:
        return redirect('/vouchers/')

    return render(request, 'gymtime/voucher_confirmdelete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatevoucher(request, pk):
    accountvoucher = Cashdet01.objects.get(primaryno=pk)
    form = Cashdet01_f(instance=accountvoucher)
    accountvouchers = Cashdet01.objects.all()
    chartsofaccounts = Customer01.objects.all()
    context = {'form': form, 'vouchers': accountvouchers,
               'voucher': accountvoucher,'chartsofaccounts': chartsofaccounts, }
    if 'save' in request.POST:
        form = Cashdet01_f(request.POST, instance=accountvoucher)
        if form.is_valid():
            form.save()
            return redirect('/vouchers/')
    if 'cancel' in request.POST:
        return redirect('/vouchers/')
    return render(request, 'gymtime/voucher_edit.html', context)


@login_required(login_url='login')
def transactions(request):
    context = {}
    form = Transaction_f()
    transactions = Transactions.objects.all()
    context = {'form': form, 'transactions': transactions}
    if 'G_submit' in request.POST:
        transactions_check = Transactions.objects.filter(
            year=request.POST.get('year'),month=request.POST.get('month'))
        members = Member.objects.filter(active=True)
        #where year = txtyear and month = txtmonth and member_code = m.code
        #where year(m.date) >= cmbyear and month(m.date) >= cmbmonth
        date = (request.POST.get('year') + "-" +
                    request.POST.get('month')+'-01')
        date = datetime.strptime(date, ('%Y-%m-%d'))
        date = date.date()
        if not transactions_check :
            for m in members:
                if m.date.strftime('%Y-%m') <= date.strftime('%Y-%m'):
                    voucherss = Cashdet01.objects.filter(
                        vouchtype='JV', entrydate=datetime.today().strftime('%Y-%m-%d'))
                    num = [0]
                    code = 0
                    for e in voucherss:
                        num.append(int(e.code))
                        code = int(max(num))
                    if(code <= 8):
                        code = "00"+str(code+1)
                    elif(code <= 99):
                        code = "0"+str(code+1)
                    elif(code >= 100):
                        code = str(code+1)
                    vocherno = 'JV' + datetime.today().strftime('%Y-%m-%d').replace('-', '')
                    #print("codetype", type(code), "Voucher no type", type(vocherno))
                    vocherno = vocherno + str(code)
                    Cashdet01Data = Cashdet01(
                        code=code,
                        salpur="salpur",
                        bill="bill",
                        date=datetime.today().strftime('%Y-%m-%d'),
                        party="030001",
                        partydescript="Receivables",
                        descript="Monthly Fee -- " + request.POST.get('month') + "-" + request.POST.get('year') + " --"+m.code +
                        "-"+m.name,
                        debit=m.totalfee,
                        credit=0,
                        vouchno=vocherno,
                        balance=0,
                        cashbalance=0,
                        balance1=0,
                        vouchtype='JV',
                        reconmark="0",
                        username=request.user,
                        entrydate=datetime.today().strftime('%Y-%m-%d'),
                        deleted='0',
                    )
                    TransactionData = Transactions(
                        year=request.POST.get('year'),
                        month=request.POST.get('month'),
                        member_code=m,
                        due_amt=m.totalfee,
                        # datetime.today().strftime('%Y-%m-%d'),
                        due_date=request.POST.get('year')+'-'+request.POST.get('month')+'-'+m.start.strftime('%d'),
                        paid_amt=0,
                        paid_date='1900-01-01',
                        balance=0,
                        vouchno=vocherno,
                        status="Due"

                    )

                    Cashdet01Data.save()
                    TransactionData.save()
            transactions = Transactions.objects.filter(
                month=request.POST.get('month'), year=request.POST.get('year'))
            context = {'form': form, 'transactions': transactions}
            return render(request, 'gymtime/transactions.html', context)
        else:     
            date = (request.POST.get('year') + "-" +
                    request.POST.get('month')+'-15')
            date = datetime.strptime(date, ('%Y-%m-%d'))
            date = date.date()
            #print(datetime.strptime(date, ('%Y-%m-%d').strftime('%Y-%m-%d')))
            for m in members:
                if m.date.strftime('%Y-%m') <= date.strftime('%Y-%m'):
                    transac = Transactions.objects.filter(
                        member_code=m, month=request.POST.get('month'), year=request.POST.get('year'))
                    if transac:
                        pass
                    else:
                        #password1 = request.POST.get('password1')
                        voucherss = Cashdet01.objects.filter(
                            vouchtype='JV', entrydate=datetime.today().strftime('%Y-%m-%d'))
                        num = [0]
                        code = 0
                        for e in voucherss:
                            num.append(int(e.code))
                            code = int(max(num))
                        if(code <= 8):
                            code = "00"+str(code+1)
                        elif(code <= 99):
                            code = "0"+str(code+1)
                        elif(code >= 100):
                            code = str(code+1)
                        vocherno = 'JV' + datetime.today().strftime('%Y-%m-%d').replace('-', '')
                        #print("codetype", type(code), "Voucher no type", type(vocherno))
                        vocherno = vocherno + str(code)
                        Cashdet01Data = Cashdet01(
                            code=code,
                            salpur="salpur",
                            bill="bill",
                            date=datetime.today().strftime('%Y-%m-%d'),
                            party="030001",
                            partydescript="Receivables",
                            descript="Monthly Fee -- " + request.POST.get('month') + "-" + request.POST.get('year') + " --"+m.code +
                            "-"+m.name,
                            debit=m.totalfee,
                            credit=0,
                            vouchno=vocherno,
                            balance=0,
                            cashbalance=0,
                            balance1=0,
                            vouchtype='JV',
                            reconmark="0",
                            username=request.user,
                            entrydate=datetime.today().strftime('%Y-%m-%d'),
                            deleted='0',
                        )
                        TransactionData = Transactions(
                            year=request.POST.get('year'),
                            month=request.POST.get('month'),
                            member_code= m,
                            due_amt=m.totalfee,
                            due_date=request.POST.get('year')+'-'+request.POST.get('month')+'-'+m.start.strftime('%d'),#datetime.today().strftime('%Y-%m-%d'),
                            paid_amt=0,
                            paid_date='1900-01-01',
                            balance = 0,
                            vouchno=vocherno,
                            status = "Due"

                        )
                    
                        Cashdet01Data.save()
                        TransactionData.save()
            transactions = Transactions.objects.filter(month=request.POST.get('month'), year=request.POST.get('year'))
            context = {'form': form, 'transactions': transactions}
            return render(request, 'gymtime/transactions.html', context)
        # transactions = Transactions.objects.all()
        # context = {'form': form, 'transactions': transactions}
        # return render(request, 'gymtime/transactions.html', context)
    context = {'form': form}
    return render(request, 'gymtime/transactions.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatetransactions(request, pk):
    Transaction = Transactions.objects.get(trans_id=pk)
    form = Transaction_f(instance=Transaction)
    transactions = "" 
    context = {'form': form,'Transaction': Transaction,'transactions': transactions }
    if 'save' in request.POST:
        form = Transaction_f(request.POST, instance=Transaction)
        print(form.errors)
        # print(form)
        if form.is_valid():
            vocherno = form.cleaned_data.get('vouchno')
            print("voucher no ", vocherno)
            Cashdet01Data = Cashdet01(
                code=vocherno[10:],
                salpur="salpur",
                bill="bill",
                date=form.cleaned_data.get('paid_date'),
                party="010001",
                partydescript="Receivables",
                descript="Monthly Fee -- " + request.POST.get('month') + "-" + request.POST.get('year') + " --"+
                "-"+str(form.cleaned_data.get('member_code')),
                debit=0,
                credit=form.cleaned_data.get('paid_amt'),
                vouchno=form.cleaned_data.get('vouchno'),
                balance=0,
                cashbalance=0,
                balance1=0,
                vouchtype='JV',
                reconmark="0",
                username=request.user,
                entrydate=datetime.today().strftime('%Y-%m-%d'),
                deleted='0',
            )
            Cashdet01Data.save()
            Cashdet02Data = Cashdet01(
                code=vocherno[10:],
                salpur="salpur",
                bill="bill",
                date=form.cleaned_data.get('paid_date'),
                party="060001",
                partydescript="Cash",
                descript="Monthly Fee -- " + request.POST.get('month') + "-" + request.POST.get('year') + " --" +
                "-"+str(form.cleaned_data.get('member_code')),
                debit=form.cleaned_data.get('paid_amt'),
                credit=0,
                vouchno=form.cleaned_data.get('vouchno'),
                balance=0,
                cashbalance=0,
                balance1=0,
                vouchtype='JV',
                reconmark="0",
                username=request.user,
                entrydate=datetime.today().strftime('%Y-%m-%d'),
                deleted='0',
            )
            Cashdet02Data.save()
            Cashdet03Data = Cashdet01(
                code=vocherno[10:],
                salpur="salpur",
                bill="bill",
                date=form.cleaned_data.get('paid_date'),
                party="070001",
                partydescript="Gym Revenue",
                descript="Monthly Fee -- " + request.POST.get('month') + "-" + request.POST.get('year') + " --" +
                "-"+str(form.cleaned_data.get('member_code')),
                debit=form.cleaned_data.get('paid_amt'),
                credit=0,
                vouchno=form.cleaned_data.get('vouchno'),
                balance=0,
                cashbalance=0,
                balance1=0,
                vouchtype='JV',
                reconmark="0",
                username=request.user,
                entrydate=datetime.today().strftime('%Y-%m-%d'),
                deleted='0',
            )
            Cashdet03Data.save()
            form.save()
            return redirect('/Transactions/')
    if 'cancel' in request.POST:
        return redirect('/Transactions/')
    return render(request, 'gymtime/transactions_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletetransactions(request, pk):
    Transaction = Transactions.objects.get(trans_id=pk)
    context = {'transaction': Transaction}
    if 'delete' in request.POST:
        Transaction.delete()
        return redirect('/Transactions/')
    elif 'cancel' in request.POST:
        return redirect('/Transactions/')

    return render(request, 'gymtime/transactions_deleteconfirmaiton.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member_search(request):
    context = {}
    if 'search_button' in request.POST and request.POST.get('search') == 'name':
        query = request.POST.get('searchhh')
        result = Member.objects.filter(name__contains=query)
        context = {'result':result}
    if 'search_button' in request.POST and request.POST.get('search') == 'cnic':
        query = request.POST.get('searchhh')
        result = Member.objects.filter(mobile__contains=query)
        context = {'result':result}
    if 'back' in request.POST:
        return redirect('/member/')
    return render(request, 'gymtime/member_search.html', context)

