import argparse

from classes.datum import Datum
from classes.settings import Settings

parser = argparse.ArgumentParser(description = 'This is filtering outlier data.')
parser.add_argument('-s', '--setting', help = 'Enter path to the setting file.')
parser.add_argument('-d', '--data', help = 'Enter path to the data file')

def main():
    args = parser.parse_args()

    settings = Settings(args.setting)
    
    datum = Datum()
    if not datum.read_raw_data(args.data):
        raise RuntimeError('There was an issue reading the data from the file.')

    datum.sanatize(settings, 'Abs')

main()
