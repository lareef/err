from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.i18n import JavaScriptCatalog
from .views import LandingPageView, ActivateAccount, SignupView, Signup, activate

app_name = 'util'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    #path('signup/', Signup, name='signup'),
    #path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('reset-password/', PasswordResetView.as_view(success_url=reverse_lazy('util:password_reset_done')), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url=reverse_lazy('util:password_reset_complete')), name='password_reset_confirm'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]