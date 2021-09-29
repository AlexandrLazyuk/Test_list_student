from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import Subject
from app.util.table import ViewTable
from app.util.repository import Subjects
import json


class Command(BaseCommand):
    CELLS = ['Id', 'name']
    help = 'CRUD subject'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-a', '--all', action='store_true', help='Show all subjects')
        parser.add_argument('-s', '--id', type=int, help='Get subject by id', nargs='?', const=1)
        parser.add_argument('-d', '--delete', action='store_true', help='Delete subject by id')
        parser.add_argument('-u', '--update', type=str, help='Update subject by id')

    def handle(self, *args, **options):
        subject_id = options['id']
        repository = Subjects(id=subject_id)
        try:
            if options['all']:
                rows = []
                for subject in repository.get_all_subjects():
                    fields = [subject.id, subject.last_name, subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                subject = repository.get_subject_by_id()
                if options['delete']:
                    subject.delete()
                    raise CommandError(f'Subject {subject_id} was delete')
                if options['update']:
                    fields = json.loads(options['update'])
                    repository.update(fields=fields, model=subject)
                    return self.stdout.write(self.style.SUCCESS(f'Subject {subject.first_name} was update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[subject.id, subject.last_name, subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except Subject.DoesNotExist as e:
            raise CommandError(e)
