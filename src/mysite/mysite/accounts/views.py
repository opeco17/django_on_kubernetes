from django.urls import reverse_lazy
from django.views.generic import CreateView

from allauth.account.views import PasswordChangeView


class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/'