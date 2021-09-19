from django.core.management.base import BaseCommand
from app.models import UserGroup


class Command(BaseCommand):
    help = 'CRUD user'

    def add_arguments(self, parser):
        parser.add_argument('users_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for user_id in options['users_ids']:
            UserGroup.objects.get(pk=user_id)
            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % user_id))