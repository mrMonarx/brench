from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect(to='/')
        else:
            form = AuthenticationForm(request)

        context = {
            'form':form
        }
        return render(request=request, template_name='accounts/login.html', context=context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(to='/loggetout')
    return render(request=request, template_name='accounts/logout.html')

def logget_out(request):
    return render(request=request, template_name='accounts/logout_view.html')

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to='/login')
    context = {
        'register_form': form
    }
    context['form'] = UserCreationForm()
    return render(request=request, template_name='accounts/register.html', context=context)