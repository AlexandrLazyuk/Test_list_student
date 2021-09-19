from django.core.management.base import BaseCommand
from app.models import Subject


class Command(BaseCommand):
    help = 'CRUD subject'

    def add_arguments(self, parser):
        parser.add_argument('subjects_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for subject_id in options['subjects_ids']:
            Subject.objects.get(pk=subject_id)
            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % subject_id))