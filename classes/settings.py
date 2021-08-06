import json

class Settings:
    HELP_TEXT = """Settings file structure (JSON):
{
    "col_name_1": {
        "upper_bound": 1.00,
        "lower_bound": 1.00
    },
    "col_name_2": {
        "upper_bound": 1.00,
        "lower_bound": 1.00
    }
}
"""

    def __init__(self, settings = {}) -> None:
        self.settings = settings

    def get_settings_for_column(self, column: str, setting: str):
        return self.settings[column][setting]

    def help() -> None:
        print(Settings.HELP_TEXT)

    def load_settings(self) -> None:
        path = input("Please enter the path to the settings file: ")

        with open(path, 'r') as file:
            self.settings = json.load(file)

        print(f"loaded the following setting file:\n{self.to_s()}")
    

    def to_s(self) -> str:
        return json.dumps(self.settings, indent = 4)
            
 