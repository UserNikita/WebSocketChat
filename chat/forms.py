from django.contrib.auth.forms import AuthenticationForm
from django import forms


class ChatAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(ChatAuthenticationForm, self).__init__(request=request, *args, **kwargs)
        # Добавляем классы к html элементам input
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
