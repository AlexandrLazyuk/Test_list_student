from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import Subject
from app.util.table import ViewTable
import json


class Command(BaseCommand):
    CELLS = ['objects', 'name', 'description']
    help = 'CRUD subjects'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-s', '--id', type=int, help='Get subject by objects', nargs='?', const=1)
        parser.add_argument('-a', '--all', action='store_true', help='Show all subjects')
        parser.add_argument('-d', '--delete', action='store_true', help='Delete subject by objects')
        parser.add_argument('-u', '--update', type=str, help='Update subject by id')

    def handle(self, *args, **options):
        subject_id = options['id']
        try:
            if options['all']:
                rows = []
                subjects = Subject.objects.filter(role_type='subject')
                for subject in subjects:
                    fields = [subject.objects, subject.name, subject.description]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                subject = Subject.objects.get(id=subject_id,role_type='student')
                if options['delete']:
                    subject.delete()
                    raise CommandError(f'Subject {subject_id} was delete')
                if json.loads(options['update']):
                    fields = options['update']
                    subject.name = fields['subject']
                    subject.save()
                    return self.stdout.write(self.style.SUCCESS('User wos update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[subject.objects, subject.name, subject.description]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except Subject.DoesNotExist:
            raise CommandError(f'Subject {subject_id} does not exist')
