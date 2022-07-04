from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

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
        return redirect(to='/logout')
    return render(request=request, template_name='accounts/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(to='/loggetout')
    return render(request=request, template_name='accounts/logout.html')

def logget_out(request):
    return render(request=request, template_name='accounts/logout_view.html')

def register_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reset = request.POST.get('confirm_password')
        # print(f"First: {fname}\nLast: {lname}\nemail: {email}\password: {password}\nreset:{reset}")
        user = authenticate(request, fname=fname, lname=lname, email=email, password=password, reset=reset)
        login(request, user)
        return redirect(to='/article')
    return render(request=request, template_name='accounts/register.html')