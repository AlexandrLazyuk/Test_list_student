from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UniversityUser
from app.util.table import ViewTable


class Command(BaseCommand):
    help = 'CRUD teacher'

    def add_arguments(self, parser):
        parser.add_argument('teachers_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for teacher_id in options['teachers_ids']:
            Subject.objects.get(pk=teacher_id)
            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % teacher_id))