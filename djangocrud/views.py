from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CustomForm
from django.contrib import messages
# Create your views here.


class HomeView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'home.html')

class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
       
       
        form = CustomForm()
        context = {
            'form':form, 
        }
        return render(request, 'sign_up.html', context)
          
    def post(self, request, *args, **kwargs):
            
        form = CustomForm(request.POST)
        try:
            if form.is_valid():
                form.save()

                messages.success(request, 'Registro completado correctamente.')

                return redirect('andre:home')

        except Exception as e: 
            form.add_error(None, "Ocurrió un error.")       
       
        return render(request, 'sign_up.html', {'form':form})