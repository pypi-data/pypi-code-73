# Generated by Django 2.1.3 on 2018-11-28 20:54

from cryptography import x509
from cryptography.hazmat.backends import default_backend

from django.conf import settings
from django.db import migrations
from django.utils.encoding import force_bytes
from django.utils import timezone


def add_valid_from(apps, schema_editor):
    Certificate = apps.get_model('django_ca', 'Certificate')
    for cert in Certificate.objects.all():
        backend = default_backend()
        pem = x509.load_pem_x509_certificate(force_bytes(cert.pub), backend)
        valid_from = pem.not_valid_before

        if settings.USE_TZ:
            valid_from = timezone.make_aware(valid_from)

        cert.valid_from = valid_from
        cert.save()

    CertificateAuthority = apps.get_model('django_ca', 'CertificateAuthority')
    for cert in CertificateAuthority.objects.all():
        backend = default_backend()
        pem = x509.load_pem_x509_certificate(force_bytes(cert.pub), backend)
        valid_from = pem.not_valid_before

        if settings.USE_TZ:
            valid_from = timezone.make_aware(valid_from)

        cert.valid_from = valid_from
        cert.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0009_auto_20181128_2050'),
    ]

    operations = [
        migrations.RunPython(add_valid_from),
    ]
