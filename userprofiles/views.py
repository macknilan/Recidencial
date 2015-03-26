# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.views.generic import TemplateView, RedirectView, FormView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.template.context import RequestContext

from userprofiles.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserForm, UserProfileForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    # success_url = '/profile/'

    def form_valid(self, form):
        login(self.request, form.user_cache)

        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):  # PASAR VARIABLES AL TEMPLATE
        context = super(LoginView, self).get_context_data(**kwargs)  # SUPER DEL PADRE
        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        data = {
            'is_auth': is_auth,
            'name': name,
        }

        context.update(data)
        return context

    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user.username})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile.html'

    def get_context_data(self, **kwargs):  # PASAR VARIABLES AL TEMPLATE
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'userprofile': self.get_userprofile()})

            return context

    def get_userprofile(self):
        return self.request.user.userprofile
        # ESTA FUNCION LO UNICO QUE HACE ES TRAER EL USERPROFILE O USER


class HomeRedirectView(RedirectView):
    pattern_name = 'login'


class PerfilRedirectView(RedirectView):
    pattern_name = 'profile'


@login_required
def EditUser_UserProfileDef(request):
    user = request.user
    profile = user.userprofile
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if all([user_form.is_valid(), profile_form.is_valid()]):
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('profile', kwargs={'slug': profile.slug}))

    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    template = "user_userprofile_update_form.html"
    return render_to_response(template, {'user_form': user_form, 'profile_form': profile_form}, context_instance=RequestContext(request))


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile_detail.html'


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_update_form.html'
    success_url = '/perfil/'


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['avatar', 'grupo']
    template_name = 'userprofile_update_form.html'
    success_url = '/perfil/'
#    slug_url_kwarg = 'slug'
#    slug_field = 'pk__userpro'
