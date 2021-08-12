from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('logout/', views.Logoutuser, name='logout'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chartofaccounts/', views.chartofaccounts, name='chartofaccounts'),
    path('chartofaccounts/<str:pk>/', views.updatechartofaccounts, name='updatechartofaccounts'),
    path('chartofaccounts/delete/<str:pk>/', views.deletechartofaccounts, name='deletechartofaccounts'),
    path('members/', views.members, name='members'),
    path('members/<str:pk>/', views.updatemember, name='updatemembers'),
    path('members/delete/<str:pk>/', views.deletemembers,
         name='deletemembers'),
    path('packages/', views.packages, name='packages'),
    path('packages/<str:pk>/', views.updatepackages, name='updatepackages'),
    path('packages/delete/<str:pk>/', views.deletepackage, name='deletepackage'),
    path('traniee/', views.trainee, name='trainee'),
    path('traniee/<int:pk>/', views.updatetrainee, name='updatetrainee'),
    path('traniee/delete/<int:pk>/', views.deletetrainee, name='deletetrainee'),
    path('vouchers/', views.accountsvouchers, name='accountsvoucher'),
    path('vouchers/old/', views.oldaccountsvouchers, name='oldaccountsvouchers'),
    path('vouchers/delete/<str:pk>/',
         views.deleteaccountsvouchers, name='deleteaccountsvouchers'),
    path('vouchers/<str:pk>/', views.updatevoucher,
         name='updatevoucher'),
    path('Transactions/', views.transactions, name='transactions'),
    path('Transactions/<str:pk>/', views.updatetransactions,
         name='updatetransactions'),
    path('Transactions/delete/<str:pk>/', views.deletetransactions,
         name='deletetransactions'),
    path('membersearch/', views.member_search, name='member_search'),
    
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
