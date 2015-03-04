# -*- coding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import CreateView, ListView
from django.views.generic.edit import ModelFormMixin
from userprofiles.mixins import LoginRequiredMixin
from .models import CasaGeneral
from casagenerales.forms import CasaGeneralForm
from casamovimientos.forms import CasaMovimientoForm, CasaMovimientoForm2
from casamovimientos.models import CasaMovimiento
from compradores.models import Comprador


class CasaGeneralCreateView(LoginRequiredMixin, CreateView):
    model = CasaGeneral
    fields = ['manzana', 'lote', 'etapa', 'status']
    template_name = 'casageneral_create_view.html'
    success_url = reverse_lazy("perfil")


@login_required
def CreateFormCasaGeneralCasaMovimientoDef(request, slug, pkslug):
    general_form = CasaGeneralForm(request.POST)
    movimiento_form = CasaMovimientoForm(request.POST)
    if request.method == 'POST':
        if all([general_form.is_valid(), movimiento_form.is_valid()]):
            general = general_form.save(commit=False)
            # GUARDATE, SALVATE, PERO NO TE INSERTES EN LA B.D. - SE INSTANCIA
            # EL OBJ
            movimiento = movimiento_form.save(commit=False)
            general.comprador = Comprador.objects.get(pk=pkslug)
            movimiento.comprador = Comprador.objects.get(pk=pkslug)
            general.save()
            movimiento.save()
            return HttpResponseRedirect(reverse('profile', kwargs={'slug': slug}))

    else:
        general_form = CasaGeneralForm()
        movimiento_form = CasaMovimientoForm()

    template = "general_movimientos_create_form.html"
    return render_to_response(template, {'general_form': general_form, 'movimiento_form': movimiento_form}, context_instance=RequestContext(request))


@login_required
def UpdateFormCasaGeneralCasaMovimientoDef(request, slug, pkslug):
    general = get_object_or_404(CasaGeneral, pk=pkslug)
    movimiento = get_object_or_404(CasaMovimiento, pk=pkslug)
    if request.method == 'POST':
        general_form = CasaGeneralForm(request.POST, instance=general)
        movimiento_form = CasaMovimientoForm2(
            request.POST, instance=movimiento)
        if all([general_form.is_valid(), movimiento_form.is_valid()]):
            general_form.save()
            movimiento_form.save()
            return HttpResponseRedirect(reverse('clienteslist', kwargs={'slug': slug}))

    else:
        general_form = CasaGeneralForm(instance=general)
        movimiento_form = CasaMovimientoForm2(instance=movimiento)

    template = "general_movimientos_update_form.html"
    return render_to_response(template, {'general_form': general_form, 'movimiento_form': movimiento_form}, context_instance=RequestContext(request))


class CompradorGeneralMovimientoList(ListView):
    model = CasaGeneral
    # slug_url_kwarg = 'slug'
    # slug_field = 'slug'
    paginate_by = 15
    template_name = "comprador_general_movimiento_list.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(
                comprador__userprofile__slug=self.kwargs['slug'])
        else:
            queryset = super(
                CompradorGeneralMovimientoList, self).get_queryset()

        return queryset
