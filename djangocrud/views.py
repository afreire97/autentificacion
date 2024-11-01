from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import  LogoutView, LoginView
from django.contrib.auth import authenticate,logout, login
from .forms import CustomForm,DiscusionForm, CustomLoginForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.


class HomeView(View):
    
    def get(self, request):

        return render(request, 'home.html')


class SignUpView(View):

    def get(self, request):
       
       
        form = CustomForm()
        context = {
            'form':form, 
        }
        return render(request, 'sign_up.html', context)
          
    def post(self, request):
            
        form = CustomForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
              
                login(request, user)
                messages.success(request, 'Registro completado correctamente.')

                return redirect('andre:home')

        except Exception as e: 

            form.add_error(None, "Ocurrió un error.")       
       
        return render(request, 'sign_up.html', {'form':form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'  # Specify the path to your login template
    success_url = reverse_lazy('andre:home')  # Replace 'home' with the name of your home URL pattern

class SignOutView(LogoutView):

    next_page = reverse_lazy('andre:home')

    
@method_decorator(login_required, name='dispatch')
class ModelCreateView(View):

    template_name = "createFight.html"
    
    def get(self, request):
        
        context = {
            'form': DiscusionForm()
        }
        
        return render(request, self.template_name, context)
    def post(self, request):
        
        form = DiscusionForm(request.POST)
        if form.is_valid():
            discusion = form.save(commit=False)
            discusion.usuario = request.user
            discusion.save()
            return redirect('andre:home')
        return render(request, self.template_name, {'form': form})
            