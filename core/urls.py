from django.urls import path


from core.views import login, register

urlpatterns = [
    path('', login),
    path('cadastro', register),
 ]