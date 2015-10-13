# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import CompradorCreateForm
from .models import Comprador
from userprofiles.mixins import LoginRequiredMixin
from userprofiles.models import UserProfile
from casagenerales.models import CasaGeneral


@login_required
def CompradorCreateDef(request, slug):
    if request.method == 'POST':
        form = CompradorCreateForm(request.POST)
        if form.is_valid():
            comprador = form.save(commit=False)
            comprador.userprofile = UserProfile.objects.get(slug=slug)
            comprador.save()
            return HttpResponseRedirect(reverse('casageneralcreate',   kwargs={'slug': slug, 'pkslug': comprador.id}))
#           return HttpResponseRedirect(reverse('casageneralcreate',  args=(slug, comprador.id,)))
#           return HttpResponseRedirect(reverse('profile', kwargs={'slug': slug}))

    else:
        form = CompradorCreateForm()

    template = "comprador_create_view.html"
    return render_to_response(template, context_instance=RequestContext(request, locals()))


class CompradorListView(LoginRequiredMixin, ListView):
    model = CasaGeneral
    template_name = "compradores_list.html"
    paginate_by = 15

    def get_queryset(self):
        if self.kwargs.get('asesor'):
#            queryset = Comprador.objects.filter()
            """
            PARA LISTAR LOS RELACIONADOS CON EL ASESOR SE TOMAN DE UNA LISTA []
            """
            queryset = self.model.objects.filter(comprador__userprofile__slug=self.kwargs['asesor'])
        else:
            queryset = super(CompradorListView, self).get_queryset()

        return queryset


class CompradorUpdateView(LoginRequiredMixin, UpdateView):
    model = Comprador
    fields = ['nombre', 'a_paterno', 'a_materno']
    template_name = 'comprador_update_view.html'

    def get_success_url(self):
        return reverse('clienteslist', kwargs={'slug': self.object.userprofile.slug})



class DeleteClienteView(LoginRequiredMixin, DeleteView):
    model = Comprador
    template_name = ("compradores_delete.html")

    def get_success_url(self):
        slug = self.request.user.userprofile.slug
        return reverse('clienteslist', kwargs={'slug': slug})



"""
class CompradorListView(LoginRequiredMixin, ListView):
    model = Comprador
    template_name = "compradores_list.html"

    def get_queryset(self):
        if self.kwargs.get('asesor'):
            # queryset = Comprador.objects.filter()
            # PARA LISTAR LOS RELACIONADOS CON EL ASESOR SE TOMAN DE UNA LISTA []
            queryset = self.model.objects.filter(userprofile__slug=self.kwargs['asesor'])
        else:
            queryset = super(CompradorListView, self).get_queryset()

        return queryset
"""

