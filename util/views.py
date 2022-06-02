from django.shortcuts import reverse, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('util:login')

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'
    
# def hello(request):
#     print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
#     return render(request, 'hello.html')
