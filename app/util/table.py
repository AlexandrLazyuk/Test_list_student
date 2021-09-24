from prettytable import PrettyTable


class ViewTable(PrettyTable):
    c_cells = []
    c_rows = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.c_cells = kwargs['c_cells']
        self.c_rows = kwargs['c_rows']

    def draw(self):
        self.field_names = self.c_cells
        self.add_rows(self.c_rows)
        return self.get_string()
