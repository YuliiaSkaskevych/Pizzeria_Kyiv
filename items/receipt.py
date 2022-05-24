from _datetime import datetime
from items.receiptline import ReceiptLine
from items.table import Table

class Receipt:

    n_Receipt = 1

    def __init__(self, table: Table):
        self.table = table
        self.datetime = datetime.now()
        self.lines = []
        self.num = Receipt.n_Receipt
        Receipt.n_Receipt += 1

    def add_line(self, line: ReceiptLine):
        self.lines.append(line)

    def __str__(self):
        a = "\n".join([str(item) for item in self.lines])
        return f'{self.datetime}' \
               f'\n{self.table} ' \
               f'\nOrder № {self.num} ' \
               f'\n{a}'

