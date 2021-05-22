from django.forms import ModelForm
from .models import CustomUser, Account, Transactions
from django import forms


class UserRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "age", "phone"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class AccountCreateForm(ModelForm):
    class Meta:
        model = Account
        fields = ["account_number", "balance", "ac_type", "user", "active_status"]


class TransactionCreateForm(forms.Form):
    user = forms.CharField()
    to_account_number = forms.CharField(widget=forms.PasswordInput)
    confirm_account_number = forms.CharField()
    amount = forms.CharField(max_length=5)
    remarks = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        to_account_number = cleaned_data.get("to_account_number")
        confirm_account_number = cleaned_data.get("confirm_account_number")
        amount = int(cleaned_data.get("amount"))
        user = cleaned_data.get("user")

        try:  # if account not present
            account = Account.objects.get(account_number=to_account_number)
        except:
            msg = "Invalid account number"
            self.add_error("to_account_number", msg)

        if to_account_number != confirm_account_number:
            msg = "account number not match"
            self.add_error("to_account_number", msg)

        account = Account.objects.get(user__username=user)  # user=1,2,3,4? but we get username therefor __username
        available_balance = account.balance
        if amount > available_balance:
            message = "Insufficient Balance"
            self.add_error("amount", message)
