from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'account/home.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'    
