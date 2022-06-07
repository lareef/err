from django.shortcuts import reverse, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, View

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import login, get_user_model
#from django.contrib.auth.models import User
from .models import UserProfile, User
from django.core.mail import EmailMessage

from django.http import HttpResponse  

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .token import account_activation_token

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'
    
class SignupView(View):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return render(request, 'registration/email_confirmation.html')
        return render(request, self.template_name, {'form': form})

def Signup(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'ERM Enterprise Resource Management - User Activation link'  
            message = render_to_string('registration/account_activation_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return render(request, 'registration/email_confirmation.html')
    else:  
        form = CustomUserCreationForm()  
    return render(request, 'registration/signup.html', {'form': form})


class ActivateAccount(View):
        
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            profile = UserProfile.objects.get(user_id=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            profile.email_confirmed = True
            profile.save()
            login(request, user)
            return render(request, 'registration/email_confirmation_done.html')
        else:
            messages.warning(request, ('Activation link is invalid !'))
            return redirect('util:login')
        
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)
        profile = UserProfile.objects.get(user_id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        # Not for this application
        #user.is_active = True
        #user.save()  
        profile.email_confirmed = True
        profile.save()
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'registration/email_confirmation_done.html')
    else:  
        return redirect('util:login')