from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.i18n import JavaScriptCatalog
from .views import LandingPageView, SignupView, hello

app_name = 'util'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('hello/', hello, name='hello'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]