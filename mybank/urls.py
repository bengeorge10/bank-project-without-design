"""bankpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Registration,LoginView,AccountCreateView,index,TransactionsView,BalanceEnq,TransactionHistory,signout

urlpatterns = [
    path('register', Registration.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('accounts', AccountCreateView.as_view(), name="accounts"),
    path('index', index, name="index"),
    path('transactions', TransactionsView.as_view(), name="transactions"),
    path('enq', BalanceEnq.as_view(), name="balance"),
    path('history', TransactionHistory.as_view(), name="history"),
    path('logout/', signout, name="logout")
]
