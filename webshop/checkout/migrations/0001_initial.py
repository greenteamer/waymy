# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 12:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type', models.CharField(choices=[(b'russian_post', b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xb0 \xd0\xa0\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd0\xb8'), (b'ems', b'EMS')], default=b'', max_length=100, verbose_name='\u0441\u043f\u043e\u0441\u043e\u0431 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('weight', models.IntegerField(default=0, verbose_name='\u0412\u0435\u0441')),
                ('delivery_price', models.DecimalField(decimal_places=0, max_digits=9)),
                ('cart_id_delivery', models.CharField(max_length=50)),
                ('gift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.GiftPrice', verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u0430\u0440\u043e\u043a')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='\u0412\u0430\u0448 email')),
                ('phone', models.CharField(max_length=20, verbose_name='\u0412\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('shipping_name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f')),
                ('shipping_address_1', models.CharField(max_length=50, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('shipping_city', models.CharField(max_length=50, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('shipping_address_2', models.CharField(blank=True, max_length=50, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441(\u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)')),
                ('shipping_country', models.CharField(max_length=50, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430')),
                ('shipping_zip', models.CharField(max_length=10, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, '\u041f\u0440\u0438\u043d\u044f\u0442\u043e'), (2, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e'), (3, '\u041e\u043f\u043b\u0430\u0442\u0430 \u043a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u0435\u0439')], default=1)),
                ('payment_method', models.IntegerField(choices=[(1, '\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c \u043a\u0432\u0438\u0442\u0430\u043d\u0446\u0438\u044e'), (2, '\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c Viza, MasterCard, \u042f\u043d\u0434\u0435\u043a\u0441\u0414\u0435\u043d\u044c\u0433\u0438')], default=2)),
                ('ip_address', models.GenericIPAddressField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=20)),
                ('delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Delivery')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('atribute', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductVolume')),
                ('feel', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.FeelName')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOneClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430')),
                ('phone', models.CharField(max_length=20, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
            ],
            options={
                'ordering': ['product_name'],
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u044b',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b \u0432 1 \u043a\u043b\u0438\u043a',
            },
        ),
    ]
