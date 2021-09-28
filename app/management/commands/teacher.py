from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UniversityUser
from app.util.table import ViewTable
import json


class Command(BaseCommand):
    CELLS = ['Id', 'Username', 'Role', 'Subject']
    help = 'CRUD teachers'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-s', '--id', type=int, help='Get teacher by id', nargs='?', const=1)
        parser.add_argument('-a', '--all', action='store_true', help='Show all teachers')
        parser.add_argument('-d', '--delete', action='store_true', help='Delete teacher by id')
        parser.add_argument('-u', '--update', type=str, help='Update teacher by id')

    def handle(self, *args, **options):
        teacher_id = options['id']
        try:
            if options['all']:
                rows = []
                teachers = UniversityUser.objects.filter(role_type='student')
                for teacher in teachers:
                    fields = [teacher.id, teacher.username, teacher.role_type, teacher.subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                teacher = UniversityUser.objects.get(id=teacher_id, role_type='teacher')
                if options['delete']:
                    teacher.delete()
                    raise CommandError(f'Teacher {teacher_id} was delete')
                if json.loads(options['update']):
                    fields = options['update']
                    teacher.username = fields['username']
                    teacher.save()
                    return self.stdout.write(self.style.SUCCESS('Teacher wos update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[teacher.id, teacher.username, teacher.role_type, teacher.subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UniversityUser.DoesNotExist:
            raise CommandError(f'Teacher {teacher_id} does not exist')
