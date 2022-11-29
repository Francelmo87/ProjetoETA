from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eta_tres.forms import EtatresForm
from eta_tres.models import EtaTres


# Create your views here.

def eta_tres_list(request):
    template_name = 'eta_tres_list.html'
    obj = EtaTres.objects.all()
    paginator = Paginator(obj, 12)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def eta_tres_add(request):
    form = EtatresForm(request.POST or None)
    template_name = 'eta_tres_add.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_tres:eta_tres_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_tres_update(request, pk):
    template_name = 'eta_tres_update.html'
    obj = EtaTres.objects.get(pk=pk)
    form = EtatresForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_tres:eta_tres_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_tres_delete(request, pk):
    obj = EtaTres.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('eta_tres:eta_tres_list'))




