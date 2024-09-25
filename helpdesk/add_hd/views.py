from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Helpdesk
from .forms import helpdeskForm, Helpdesk


class UserListView(ListView):
    model = user
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = user
    template_name = 'user_detail.html'

class UserCreateView(CreateView):
    model = user
    form_class = helpdeskForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = user
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = user
    form_class = helpdeskForm
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user_list')

def hd_list(request):
    helpdesks = Helpdesk.objects.all()
    return render(request, "HD_list.html", {"helpdesks":helpdesks})