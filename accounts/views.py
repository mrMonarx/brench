from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username: {username}\npassword: {password}")
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {'error': 'Siz hali ro`yxatdan o`tmagansiz'}
            return render(request=request, template_name='accounts/login.html', context=context)
        login(request, user)
        return redirect(to='/admin')
    return render(request=request, template_name='accounts/login.html')

def logout_view(request):
    return render(request=request, template_name='accounts/logout.html')

def register_view(request):
    return render(request=request, template_name='accounts/register.html')