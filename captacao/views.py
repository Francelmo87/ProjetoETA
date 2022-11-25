from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from captacao.forms import CaptacaoForm
from captacao.models import Captacao


# Create your views here.


def captacao_list(request):
    template_name = 'captacao_list.html'
    obj_list = Captacao.objects.all()

    paginator = Paginator(obj_list, 3)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def captacao_add(request):
    form = CaptacaoForm(request.POST or None)
    template_name = 'captacao_add.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('captacao:captacao_list'))

    context = {'form': form}
    return render(request, template_name, context)


def captacao_update(request, pk):
    template_name = 'captacao_update.html'
    obj = Captacao.objects.get(pk=pk)
    form = CaptacaoForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('captacao:captacao_list'))

    context = {'form': form}
    return render(request, template_name, context)


def captacao_delete(request, pk):
    obj = Captacao.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('captacao:captacao_list'))