from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from saida.forms import SaidaForm
from saida.models import Saida


# Create your views here.


def saida_list(request):
    template_name = 'saida_list.html'
    obj = Saida.objects.all()

    paginator = Paginator(obj, 12)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def saida_add(request):
    form = SaidaForm(request.POST or None)
    template_name = 'saida_add.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('saida:saida_list'))

    context = {'form': form}
    return render(request, template_name, context)


def saida_update(request, pk):
    template_name = 'saida_update.html'
    obj = Saida.objects.get(pk=pk)
    form = SaidaForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('saida:saida_list'))

    context = {'form': form}
    return render(request, template_name, context)


def saida_delete(request, pk):
    obj = Saida.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('saida:saida_list'))