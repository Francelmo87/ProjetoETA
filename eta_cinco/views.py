from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eta_cinco.forms import EtaCincoForm
from eta_cinco.models import EtaCinco


# Create your views here.

def eta_cinco_list(request):
    template_name = 'eta_cinco_list.html'
    obj = EtaCinco.objects.all()

    paginator = Paginator(obj, 12)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def eta_cinco_add(request):
    form = EtaCincoForm(request.POST or None)
    template_name = 'eta_cinco_add.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_cinco:eta_cinco_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_cinco_update(request, pk):
    template_name = 'eta_cinco_update.html'
    obj = EtaCinco.objects.get(pk=pk)
    form = EtaCincoForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_cinco:eta_cinco_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_cinco_delete(request, pk):
    obj = EtaCinco.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('eta_cinco:eta_cinco_list'))




