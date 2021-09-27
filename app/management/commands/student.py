from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UniversityUser
from app.util.table import ViewTable
from app.util.repository import Students
import json


class Command(BaseCommand):
    CELLS = ['Id', 'UserName', 'LastName', 'Role', 'Subject']
    help = 'CRUD students'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-a', '--all', action='store_true', help='Show all students')
        parser.add_argument('-s', '--id', type=int, help='Get student by id', nargs='?', const=1)
        parser.add_argument('-d', '--delete', action='store_true', help='Delete student by id')
        parser.add_argument('-u', '--update', type=str, help='Update student by id')

    def handle(self, *args, **options):
        student_id = options['id']
        repository = Students(id=student_id)
        try:
            if options['all']:
                rows = []
                for student in repository.get_all_students():
                    fields = [student.id, student.last_name, student.username, student.role_type, student.subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                student = repository.get_student_by_id()
                if options['delete']:
                    student.delete()
                    raise CommandError(f'User {student_id} was delete')
                if options['update']:
                    fields = json.loads(options['update'])
                    if fields['username']:
                        student.username = fields['username']
                    if fields['first_name']:
                        student.first_name = fields['first_name']
                    if fields['last_name']:
                        student.last_name = fields['last_name']
                    if fields:
                        student.save()
                    return self.stdout.write(self.style.SUCCESS(f'User {student.first_name} was update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[student.id, student.username, student.last_name, student.role_type, student.subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UniversityUser.DoesNotExist:
            raise CommandError(f'User {student_id} does not exist')
