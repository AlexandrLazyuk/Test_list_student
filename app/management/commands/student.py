from django.core.management.base import BaseCommand
from app.models import Subject


class Command(BaseCommand):
    help = 'CRUD student'

    def add_arguments(self, parser):
        parser.add_argument('students_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for student_id in options['students_ids']:
            Subject.objects.get(pk=student_id)
            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % student_id))