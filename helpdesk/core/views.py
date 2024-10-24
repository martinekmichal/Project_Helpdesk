from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required




def home_page(request):
    return render(request, "home.html")

def about_page(request):
    return render(request, "about.html")

def hd_list_page(request):
    return render(request, "HD_list.html")

@login_required
def profile_page(request):
    return render(request, 'profile.html')

def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'register.html',
                  {'form': UserRegisterForm()})

#def hd_list(request):
#    helpdesks = Helpdesk.objects.all()
#    return render(request, "HDD_list.html", {"helpdesks":helpdesks})