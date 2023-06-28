from django.urls import include, path

from .views import LoginView, RegistrationView, LogoutView


urlpatterns = [
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
    
]