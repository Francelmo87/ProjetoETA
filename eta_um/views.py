from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eta_um.forms import EtaUmForm
from eta_um.models import EtaUm


# Create your views here.


def eta_um_list(request):
    template_name = 'eta_um_list.html'
    obj = EtaUm.objects.all()
    context = {'object_list': obj}
    return render(request, template_name, context)


def eta_um_add(request):
    form = EtaUmForm(request.POST or None)
    template_name = 'eta_um_add.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_um_update(request, pk):
    template_name = 'eta_um_update.html'
    obj = EtaUm.objects.get(pk=pk)
    form = EtaUmForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_um_delete(request, pk):
    obj = EtaUm.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('eta_um:eta_um_list'))
