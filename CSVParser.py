import csv


class CSVParser:
    def __init__(self, file_name):
        self.input_file = open(file_name, 'r')
        self.csv_file = csv.DictReader(self.input_file)

    def next_line(self):
        next_line = next(self.csv_file, None)
        if not next_line:
            self.input_file.close()
        return next_line

    def all_as_dict(self):
        all_rows = {}
        current_line = self.next_line()
        while current_line:
            all_rows[current_line['id']] = current_line
            current_line = self.next_line()
        return all_rows
