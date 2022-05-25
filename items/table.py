
class Table:

    def __init__(self, number_of_table: int, persons, location):
        self.number_of_table = number_of_table
        self.persons = persons
        self.location = location

    def __str__(self):
        return f'Table № {self.number_of_table}'

