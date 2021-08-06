from classes.datum import Datum
from classes.settings import Settings

def main():
    settings = Settings()
    settings.load_settings()
    
    datum = Datum()
    if not datum.read_raw_data():
        raise RuntimeError("There was an issue reading the data from the file.")


    datum.sanatize(settings, 'abs')

main()