from django.shortcuts import render, redirect
from services.models import Service
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from .forms import ServiceForm

# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin requeridad que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
 
class ServiceListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service

@method_decorator(staff_member_required, name='dispatch')
class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:services')

@method_decorator(staff_member_required, name='dispatch')
class ServiceUpdate(UpdateView):
    model = Service
    fields = ['title', 'subtitle', 'content', 'image']
    template_name_suffix = '_update_form'
 
    def get_success_url(self):
        return reverse_lazy('services:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services:services')