from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UniversityUser
from app.util.table import ViewTable
from app.util.repository import Teachers
import json


class Command(BaseCommand):
    CELLS = ['Id', 'UserName', 'LastName', 'Role', 'Subject']
    help = 'CRUD teachers'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-a', '--all', action='store_true', help='Show all teachers')
        parser.add_argument('-s', '--id', type=int, help='Get teacher by id', nargs='?', const=1)
        parser.add_argument('-d', '--delete', action='store_true', help='Delete teacher by id')
        parser.add_argument('-u', '--update', type=str, help='Update teacher by id')

    def handle(self, *args, **options):
        teacher_id = options['id']
        repository = Teachers(id=teacher_id)
        try:
            if options['all']:
                rows = []
                for teacher in repository.get_all_teachers():
                    fields = [teacher.id, teacher.last_name, teacher.username, teacher.role_type, teacher.subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                teacher = repository.get_teacher_by_id()
                if options['delete']:
                    teacher.delete()
                    raise CommandError(f'Teacher {teacher_id} was delete')
                if options['update']:
                    fields = json.loads(options['update'])
                    repository.update(fields=fields, model=teacher)
                    return self.stdout.write(self.style.SUCCESS(f'Teacher {teacher.first_name} was update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[teacher.id, teacher.username, teacher.last_name, teacher.role_type, teacher.subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UniversityUser.DoesNotExist as e:
            raise CommandError(e)
