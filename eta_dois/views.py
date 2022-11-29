from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eta_dois.forms import EtaDoisForm
from eta_dois.models import EtaDois


# Create your views here.

def eta_dois_list(request):
    template_name = 'eta_dois_list.html'
    obj = EtaDois.objects.all()

    paginator = Paginator(obj, 12)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def eta_dois_add(request):
    form = EtaDoisForm(request.POST or None)
    template_name = 'eta_dois_add.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_dois:eta_dois_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_dois_update(request, pk):
    template_name = 'eta_dois_update.html'
    obj = EtaDois.objects.get(pk=pk)
    form = EtaDoisForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eta_dois:eta_dois_list'))
    context = {'form': form}
    return render(request, template_name, context)


def eta_dois_delete(request, pk):
    obj = EtaDois.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('eta_dois:eta_dois_list'))



