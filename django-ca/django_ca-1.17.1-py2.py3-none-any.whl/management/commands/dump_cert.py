# This file is part of django-ca (https://github.com/mathiasertl/django-ca).
#
# django-ca is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# django-ca is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-ca.  If not,
# see <http://www.gnu.org/licenses/>.

"""Management command to write a certificates public key to stdout or a file.

.. seealso:: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
"""

from cryptography.hazmat.primitives.serialization import Encoding

from django.core.management.base import CommandError

from ..base import CertCommand


class Command(CertCommand):  # pylint: disable=missing-class-docstring
    allow_revoked = True
    binary_output = True
    help = "Dump a certificate to a file."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        self.add_format(parser)
        parser.add_argument('-b', '--bundle', default=False, action='store_true',
                            help="Dump the whole certificate bundle.")
        parser.add_argument('path', nargs='?', default='-',
                            help='Path where to dump the certificate. Use "-" for stdout.')

    def handle(self, cert, path, **options):  # pylint: disable=arguments-differ
        if options['bundle'] and options['format'] == Encoding.DER:
            raise CommandError('Cannot dump bundle when using DER format.')

        if options['bundle']:
            certs = cert.bundle
        else:
            certs = [cert]

        self.dump(path, b''.join([c.dump_certificate(options['format']) for c in certs]))
