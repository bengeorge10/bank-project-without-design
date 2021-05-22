from .models import Account
from django.contrib import messages
from django.shortcuts import redirect

def account_validator(func):
    def wrapper(request, *args, **kwargs):
        try:
            account_details = Account.objects.get(user=request.user)
            status = account_details.active_status
            if status == "active":
                messages.error(request, 'Account already exists')
                return redirect("index")
            else:
                return func(request, *args, **kwargs)
        except:
            return func(request, *args, **kwargs)
    return wrapper
