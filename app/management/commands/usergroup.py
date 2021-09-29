from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from app.models import UserGroup
from app.util.table import ViewTable
from app.util.repository import Groups
import json


class Command(BaseCommand):
    CELLS = ['Id', 'Name']
    help = 'CRUD groups'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-a', '--all', action='store_true', help='Show all groups')
        parser.add_argument('-s', '--id', type=int, help='Get group by id', nargs='?', const=1)
        parser.add_argument('-d', '--delete', action='store_true', help='Delete group by id')
        parser.add_argument('-u', '--update', type=str, help='Update group by id')

    def handle(self, *args, **options):
        group_id = options['id']
        repository = Groups(id=group_id)
        try:
            if options['all']:
                rows = []
                for group in repository.get_all_groups():
                    fields = [group.id, group.last_name]
                    rows.append(fields)
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=rows
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))
            else:
                group = repository.get_group_by_id()
                if options['delete']:
                    group.delete()
                    raise CommandError(f'User {group_id} was delete')
                if options['update']:
                    fields = json.loads(options['update'])
                    repository.update(fields=fields, model=group)
                    return self.stdout.write(self.style.SUCCESS(f'User {group.first_name} was update'))
                table = ViewTable(
                    c_cells=self.CELLS,
                    c_rows=[[group.id, group.last_name]]
                )
                self.stdout.write(self.style.HTTP_NOT_MODIFIED(table.draw()))

        except UserGroup.DoesNotExist as e:
            raise CommandError(e)
