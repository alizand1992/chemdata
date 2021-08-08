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

    def __init__(self, path = None) -> None:
        self.settings = {}

        if path != None:
            self.settings = Settings.setting_as_dict(path)

        print(f"loaded the following setting file:\n{self.to_s()}")

    def get_settings_for_column(self, column: str, setting: str):
        return self.settings[column][setting]

    def help() -> None:
        print(Settings.HELP_TEXT)

    def load_settings(self, path = None) -> None:
        if path == None:
            path = input("Please enter the path to the settings file: ")

        self.settings = self.setting_as_dict(path)
        print(f"loaded the following setting file:\n{self.to_s()}")

    def to_s(self) -> str:
        return json.dumps(self.settings, indent = 4)
            
    def setting_as_dict(path):
        with open(path, 'r') as file:
            return json.load(file)
