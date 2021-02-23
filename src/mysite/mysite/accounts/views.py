from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model

from allauth.account.views import PasswordChangeView

from .forms import ProfileForm


class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/'
    
    
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404('プロフィールが存在しません')
        
        profile = get_object_or_404(get_user_model(), id=request.user.id)
        form = ProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'account/profile.html', context)
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404('プロフィールが存在しません')
        
        profile = get_object_or_404(get_user_model(), id=request.user.id)
        form = ProfileForm(request.POST, instance=profile)
        if not form.is_valid():
            context = {'form': form}
            messages.error(request, 'プロフィールを正しく入力して下さい', extra_tags='danger')
            return render(request, 'account/profile.html', context)
    
        form.save(commit=True)
        context = {'form': form}
        messages.info(request, 'プロフィールを変更しました', extra_tags='info')
        return render(request, 'account/profile.html', context)