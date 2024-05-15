# decorators.py

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import CustomUser

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role == CustomUser.MANAGER:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role == CustomUser.ADMIN:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper
