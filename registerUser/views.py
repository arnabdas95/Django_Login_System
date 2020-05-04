#register new user
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignUpForm, ExtraForm



def index(request):
    return render(request,'index.html')


#new user registration or signup view
def registerUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            extra_form =ExtraForm(request.POST, request.FILES)
            if form.is_valid() and extra_form.is_valid():
               user= form.save()
               #commit =false because we have to assign foreign key to the extraform
               ef=extra_form.save(commit=False)
               ef.user=user
               extra_form.full_clean()
               ef.save()

               #after successfully created new account user is logged in
               login(request, user)
               messages.success(request, f'Welcome {user}! your account is created successfully')
               return redirect('/')

        else:
            form = SignUpForm()
            extra_form = ExtraForm()
        return render(request, 'registerUser.html', {'form': form,'extra_form':extra_form})

    else:
        return redirect('/')

#logout current user
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('/')

