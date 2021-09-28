from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UserGroup
from app.util.table import ViewTable
import json


class Command(BaseCommand):
    CELLS = ['Id', 'Usergroup', 'Subject']
    help = 'CRUD groups'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-s', '--id', type=int, help='Get group by id', nargs='?', const=1)
        parser.add_argument('-a', '--all', action='store_true', help='Show all groups')
        parser.add_argument('-d', '--delete', action='store_true', help='Delete group by id')
        parser.add_argument('-u', '--update', type=str, help='Update group by id')

    def handle(self, *args, **options):
        group_id = options['id']
        try:
            if options['all']:
                rows = []
                groups = UserGroup.objects.filter(role_type='group')
                for group in groups:
                    fields = [group.id, group.usergroup, group.role_type, group.subject.name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                group = UserGroup.objects.get(id=group_id, role_type='group')
                if options['delete']:
                    group.delete()
                    raise CommandError(f'Group {group_id} was delete')
                if json.loads(options['update']):
                    fields = options['update']
                    group.usergroup = fields['usergroup']
                    group.save()
                    return self.stdout.write(self.style.SUCCESS('Group was update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[group.id, group.usergroup, group.role_type, group.subject.name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UserGroup.DoesNotExist:
            raise CommandError(f'Group {group_id} does not exist')
