from app.models import UniversityUser


class Students:
    id = 0
    TYPE = 'student'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', self.id)

    def get_all_students(self):
        students = UniversityUser.objects.filter(role_type=self.TYPE).order_by('-id')
        if not students:
            raise UniversityUser.DoesNotExist('Users do not exist')
        return students

    def get_student_by_id(self):
        try:
            return UniversityUser.objects.get(id=self.id, role_type=self.TYPE)
        except UniversityUser.DoesNotExist:
            raise UniversityUser.DoesNotExist(f'User {self.id} does not exist')

    @staticmethod
    def update(fields: dict, model: UniversityUser):
        if fields['username']:
            model.username = fields['username']
        if fields['first_name']:
            model.first_name = fields['first_name']
        if fields['last_name']:
            model.last_name = fields['last_name']
        if fields:
            model.save()


