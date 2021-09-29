from app.models import UniversityUser, UserGroup, Subject


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


class Teachers:
    id = 0
    TYPE = 'teacher'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', self.id)

    def get_all_teachers(self):
        teachers = UniversityUser.objects.filter(role_type=self.TYPE).order_by('-id')
        if not teachers:
            raise UniversityUser.DoesNotExist('Teachers do not exist')
        return teachers

    def get_teacher_by_id(self):
        try:
            return UniversityUser.objects.get(id=self.id, role_type=self.TYPE)
        except UniversityUser.DoesNotExist:
            raise UniversityUser.DoesNotExist(f'Teacher {self.id} does not exist')

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


class Groups:
    id = 0
    TYPE = 'group'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', self.id)

    def get_all_groups(self):
        groups = UserGroup.objects.filter(role_type=self.TYPE).order_by('-id')
        if not groups:
            raise UserGroup.DoesNotExist('Groups do not exist')
        return groups

    def get_group_by_id(self):
        try:
            return UserGroup.objects.get(id=self.id, role_type=self.TYPE)
        except UserGroup.DoesNotExist:
            raise UserGroup.DoesNotExist(f'User {self.id} does not exist')

    @staticmethod
    def update(fields: dict, model: UserGroup):
        if fields['name']:
            model.name = fields['name']
            model.save()


class Subjects:
    id = 0
    TYPE = 'subject'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', self.id)

    def get_all_subjects(self):
        subjects = Subject.objects.filter(role_type=self.TYPE).order_by('-id')
        if not subjects:
            raise Subject.DoesNotExist('Subjects do not exist')
        return subjects

    def get_subject_by_id(self):
        try:
            return Subject.objects.get(id=self.id, role_type=self.TYPE)
        except Subject.DoesNotExist:
            raise Subject.DoesNotExist(f'Subject {self.id} does not exist')

    @staticmethod
    def update(fields: dict, model: UniversityUser):
        if fields['name']:
            model.username = fields['name']
        if fields['objects']:
            model.first_name = fields['objects']
        if fields['description']:
            model.last_name = fields['description']
            model.save()