from django import forms
from django.contrib.auth import get_user_model


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['email', 'date_joined', 'last_login']:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')