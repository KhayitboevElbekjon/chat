
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view()),
    path('chat/',Chat.as_view()),
    path('register/',register),
    path('logaut/',Logaut),
    path('chatdelete/<int:pk>',delete)
]
