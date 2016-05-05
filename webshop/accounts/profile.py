# -*- coding: utf-8 -*-
#!/usr/bin/env python
from webshop.accounts.models import UserProfile
from webshop.accounts.forms import UserProfileForm
# from django.contrib.auth import User


def retrieve(request):
    """Возвращает экземпляр класса форма профиля пользователя"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    # если у пользователя не было профиля, то создаем его
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    return profile

def set(request):
    """Заполняем форму данными пользователя"""
    profile = retrieve(request)
    profile_form = UserProfileForm(request.POST, instance=profile)
    profile_form.save()
