# -*- coding: utf-8 -*-
#!/usr/bin/env python
import datetime
import re

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import email_re
from django.utils.encoding import smart_unicode

from webshop import settings
from models import Order

# Наше поле для валидации
# class PhoneField(forms.Field):
#     def validate(self, value):
#         super(PhoneField, self).validate(value)
#         # Проверяем на соответствие поля телефонному номеру
#         if re.compile("^([0-9\(\)\/\+ \-]*)$").search(smart_unicode(value)):
#             pass
#         # Если не соответствует ничему, то вызываем ошибку
#         else:
#             raise forms.ValidationError(_(u'Enter a valid email or phone number.'), code='invalid')


class ContactForm(forms.ModelForm):

    # payment_method =  forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user', 'transaction_id', 'delivery', 'cupon',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # переопределяем аттрибуты по умолчанию
        self.fields['payment_method'].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '30'

    def clean_phone(self):
        """Проверка телефонного номера (>10 цифр)"""
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 11:
            raise forms.ValidationError(_(u"""
            Введите правильный телефон, например (8-920-351-21-21 или 89203512121)"""))
        return self.cleaned_data['phone']

def strip_non_numbers(data):
    """Удаляет все символы которые не являются числом
    >>> strip_non_numbers('988f2ds2')
    '98822'
    """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)




class CheckoutForm(forms.ModelForm):
    """Форма оформления заказа"""
    # credit_card_number = forms.CharField()
    # credit_card_type = forms.CharField(widget=forms.Select(choices=CARD_TYPES))
    # credit_card_expire_month = forms.CharField(widget=forms.Select(choices=cc_expire_months()))
    # credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years()))
    # credit_card_cvv = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super(CheckoutForm, self).__init__(*args, **kwargs)
    #     # переопределяем аттрибуты по умолчанию
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['size'] = '30'
    #     self.fields['shipping_zip'].widget.attrs['size'] = '6'
        # self.fields['billing_zip'].widget.attrs['size'] = '6'
        # self.fields['credit_card_type'].widget.attrs['size'] = '1'
        # self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
        # self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
        # self.fields['credit_card_cvv'].widget.attrs['size'] = '5'

    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user', 'transaction_id',)


    # def clean_credit_card_number(self):
    #     """Проверка кредитной карты"""
    #     cc_number = self.cleaned_data['credit_card_number']
    #     stripped_cc_number = strip_non_numbers(cc_number)
    #     # Проверка делается только если выключена отладка
    #     if not settings.DEBUG:
    #         if not cardLuhnChecksumIsValid(stripped_cc_number):
    #             raise forms.ValidationError(_(u'The credit card you entered is invalid.'))

    # def clean_phone(self):
    #     """Проверка телефонного номера (>10 цифр)"""
    #     phone = self.cleaned_data['phone']
    #     stripped_phone = strip_non_numbers(phone)
    #     if len(stripped_phone) < 11:
    #         raise forms.ValidationError(_(u"""
    #         Enter a valid phone number with area code.(e.g.8-920-351-21-21)"""))
    #     return self.cleaned_data['phone']

class DeliveryForm(forms.Form):
    # name = forms.CharField(max_length=30, label=u'Имя')
    CHOICES=[('SPSurface', 'Small Packet Surface 25-40 дней'),
            ('SPSAL', 'Small Packet SAL 3-4 недели'),
            ('SPA' ,'Small Packet Air 2-3 недели'),
            ('PS', 'Parcel Surface 25-30 дней'),
            ('EMS', 'EMS 7-10 дней'),]

    delivery = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'onClick':'calc_delivery();'}))


