# -*- coding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from userprofiles.mixins import LoginRequiredMixin
from .models import CasaGeneral
from casagenerales.forms import CasaGeneralForm
from casamovimientos.forms import CasaMovimientoForm
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
            # GUARDATE, SALVATE, PERO NO TE INSERTES EN LA B.D. - SE INSTANCIA EL OBJ
            general = general_form.save(commit=False)
            # GUARDATE, SALVATE, PERO NO TE INSERTES EN LA B.D. - SE INSTANCIA EL OBJ
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
        movimiento_form = CasaMovimientoForm(request.POST, instance=movimiento)
        if all([general_form.is_valid(), movimiento_form.is_valid()]):
            general_form.save()
            movimiento_form.save()
            return HttpResponseRedirect(reverse('clienteslist', kwargs={'slug': slug}))

    else:
        general_form = CasaGeneralForm(instance=general)
        movimiento_form = CasaMovimientoForm(instance=movimiento)

    template = "general_movimientos_update_form.html"
    return render_to_response(template, {'general_form': general_form, 'movimiento_form': movimiento_form}, context_instance=RequestContext(request))


"""
EJEMPLOS A TOMAR

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.asesor = Comprador.objects.get(asesor__slug=self.kwargs.get(self.slug_url_kwarg, None))
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


@login_required
def EditUser_UserProfileDef(request):
    user = request.user
    profile = user.userprofile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if all ([user_form.is_valid(), profile_form.is_valid()]):
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse
                ('profile', kwargs={'slug': profile.slug}))


    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    template = "user_userprofile_update_form.html"
    return render_to_response(template, {'user_form': user_form, 'profile_form': profile_form}, context_instance=RequestContext(request))

        form.comprador = Comprador.objects.get(asesor=self.kwargs.get(self.slug_url_kwarg))
        form.instance.comprador = get_object_or_404(Comprador, asesor=self.kwargs.get(self.slug_url_kwarg))
        return super(CasaGeneralCreateView, self).form_valid(form)
"""
