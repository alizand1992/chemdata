class DataPoint:
    def __init__(self, data = {}) -> None:
        self.data = data

    def get_data(self, column: str):
        return self.data[column]