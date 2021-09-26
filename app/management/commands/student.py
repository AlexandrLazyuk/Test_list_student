from argparse import ArgumentParser
from django.core.management.base import BaseCommand,CommandError
from app.models import UniversityUser
from app.util.table import ViewTable
import json


class Command(BaseCommand):
    CELLS = ['Id','Username','Role','Subject']
    help = 'CRUD students'

    def add_arguments(self,parser: ArgumentParser):
        parser.add_argument('-s', '--id', type=int, help='Get student by id', nargs='?', const=1)
        parser.add_argument('-a', '--all', action='store_true', help='Show all students')
        parser.add_argument('-d', '--delete', action='store_true', help='Delete student by id')
        parser.add_argument('-u', '--update', type=str, help='Update student by id')

    def handle(self,*args,**options):
        student_id = options['id']
        try:
            if options['all']:
                rows = []
                students = UniversityUser.objects.filter(role_type='student')
                for student in students:
                    fields = [student.id,student.username,student.role_type,student.subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                student = UniversityUser.objects.get(id=student_id,role_type='student')
                if options['delete']:
                    student.delete()
                    raise CommandError(f'User {student_id} was delete')
                if json.loads(options['update']):
                    fields = options['update']
                    student.username = fields['username']
                    student.save()
                    return self.stdout.write(self.style.SUCCESS('User wos update'))
                table = ViewTable(
                    c_cells = self.CELLS,
                    c_rows = [[student.id, student.username, student.role_type, student.subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UniversityUser.DoesNotExist:
            raise CommandError(f'User {student_id} does not exist')
