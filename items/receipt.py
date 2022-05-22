from _datetime import datetime
from items.receiptline import ReceiptLine
from items.table import Table

class Receipt:

    n_Receipt = 1

    def __init__(self, table: Table):
        self.table = table
        self.datetime = datetime.now()
        self.lines = []
        Receipt.n_Receipt += 1

    def add_line(self, line: ReceiptLine):
        self.lines.append(line)

    def __str__(self):
        return f'{self.datetime} {self.table} \n{" ".join([str(item) for item in self.lines])}'

