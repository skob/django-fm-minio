#!env python

from datetime import datetime

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils.text import slugify

from fixtures_minio.conf import settings

from minio import Minio
from minio.error import ResponseError

from tempfile import NamedTemporaryFile

CLIENT = Minio(settings.FM_MINIO_URL,
                    access_key=settings.FM_MINIO_ACCESS_KEY,
                    secret_key=settings.FM_MINIO_SECRET_KEY,
                    secure=settings.FM_MINIO_SECURE)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'args', metavar='app_label[.ModelName]', nargs='*',
            help='Restricts dumped data to the specified app_label or app_label.ModelName.',
        )

    def get_fixture_file(self, dumpdata_args):
        fixture_file = NamedTemporaryFile(suffix='.json')
        call_command('dumpdata', *dumpdata_args, output=fixture_file.name)
        fixture_file.seek(0)
        return fixture_file

    def get_file_name(self):
        return 'fixture_{}.json'.format(
            slugify(int(datetime.utcnow().timestamp()))
        )

    def handle(self, *args, **options):
        filename = self.get_file_name()
        tmpfile = self.get_fixture_file(args)
        try:
            CLIENT.fput_object(settings.FM_MINIO_BUCKET, filename, tmpfile.name)
        except ResponseError as err:
            tmpfile.close()
        tmpfile.close()
        print('filename: %s' % filename)
