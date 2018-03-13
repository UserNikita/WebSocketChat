from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from chat.views import ChatRoomView, ChatLoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ChatLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', ChatRoomView.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
