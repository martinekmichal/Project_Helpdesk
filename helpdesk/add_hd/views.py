from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import HelpdeskForm, Helpdesk
from django.contrib.auth.models import User
from .models import Helpdesk
from django.shortcuts import render, redirect, get_object_or_404




class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = HelpdeskForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = HelpdeskForm
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user_list')


def helpdesk_create(request):
    if request.method == 'POST':
        form = HelpdeskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HDD_list')
    else:
        form = HelpdeskForm()

    return render(request, 'HD_create.html', {'form': form})

def helpdesk_list(request):
    helpdesks = Helpdesk.objects.all()
    return render(request, 'HDD_list.html', {'helpdesks': helpdesks})


class HelpdeskUpdateView(UpdateView):
    model = Helpdesk
    form_class = HelpdeskForm
    template_name = 'HD_edit.html'
    success_url = reverse_lazy('HDD_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upravit požadavek'
        return context


class HelpdeskDeleteView(DeleteView):
    model = Helpdesk
    template_name = 'HD_delete.html'
    success_url = reverse_lazy('HDD_list')