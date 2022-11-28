from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eta_quatro.forms import EtaQuatroForm
from eta_quatro.models import EtaQuatro


# Create your views here.

def eta_quatro_list(request):
    template_name = 'eta_quatro_list.html'
    obj = EtaQuatro.objects.all()

    paginator = Paginator(obj, 12)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def eta_quatro_add(request):
    form = EtaQuatroForm(request.POST or None)
    template_name = 'eta_quatro_add.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_quatro:eta_quatro_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_quatro_update(request, pk):
    template_name = 'eta_quatro_update.html'
    obj = EtaQuatro.objects.get(pk=pk)
    form = EtaQuatroForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_quatro:eta_quatro_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_quatro_delete(request, pk):
    obj = EtaQuatro.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('eta_quatro:eta_quatro_list'))




