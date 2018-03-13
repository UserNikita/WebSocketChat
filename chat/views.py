from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from chat.forms import ChatAuthenticationForm


class ChatLoginView(LoginView):
    """Переопределённое представление для авторизации"""
    template_name = 'login.html'
    form_class = ChatAuthenticationForm


class ChatRoomView(LoginRequiredMixin, TemplateView):
    """Представление для отображения основной страницы чата"""
    template_name = 'chat.html'
