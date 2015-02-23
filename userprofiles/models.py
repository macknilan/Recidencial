# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# from django.conf import settings
# from django.utils.translation import ugettext_lazy as _


class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        count = 2

        slug = slug_text
        while(model._default_manager.filter(slug=slug).exists()):
            slug = '{0}-{1}'.format(slug_text, count)

        return slug


class UserProfile(SlugMixin, models.Model):
    GRUPO = (
        (0, 'Sin grupo'),
        (1, 'Grupo uno'),
        (2, 'Grupo dos'),
        (3, 'Grupo tres'),
        )
    avatar = models.ImageField(upload_to='avatars', blank=True)
    grupo = models.IntegerField("Grupo", max_length=2, choices=GRUPO, default=0)
    slug = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.slug
        """return "%s - %s - %s - %s" % (self.user.username, self.slug, self.grupo, self.avatar)"""

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.user.username, UserProfile)
        super(UserProfile, self).save(*args, **kwargs)
