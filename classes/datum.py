from .data_point import DataPoint
from .settings import Settings

class Datum:
    dirty = False

    def __init__(self, raw_datum = []) -> None:
        self.raw_datum = raw_datum
        self.datum = []
        self.dirty = True

    def sanatize(self, setting: Settings, column: str) -> None:
        self.datum = []
        for data_point in self.raw_datum:
            col_val = data_point.get_data(column)

            if col_val < setting.get_settings_for_column(column, 'upper_bound') and col_val > setting.get_settings_for_column(column, 'lower_bound'):
                self.datum.append(data_point)

    def get_sanatized_data(self, setting: Settings = None, column: str = None):
        if not self.datum and setting != None and column != None:
            self.sanatize(setting, column)

        if not self.datum:
            raise ValueError('Please pass in Settings and Columns or Sanitize first')

        return self.datum

    def read_raw_data(self) -> bool:
        path = input("Plesae enter the path to the csv file: ")

        with open(path, 'r') as file:
            lines = file.readlines()

            columns = []

            for line in lines:
                parts = line.split(',')

                if not columns:
                    for col in parts:
                        columns.append(col)

                    continue

                self.append_data_point(columns, parts)

        return True
        
                
    def append_data_point(self, columns, parts):
        data = {}
        num_cols = len(columns)

        for col in range(num_cols):
            data[columns[col]] = parts[col]

        self.raw_datum.append(DataPoint(data))
