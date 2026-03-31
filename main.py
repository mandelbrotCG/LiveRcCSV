import os
from src.helpers import *
from src.csvCreator import CsvCreator

config = load_config('config.txt')
print(config)

creator = CsvCreator(os.getcwd(), config["baseURL"], config["startDate"])

creator.create_csvs(config["userName"])
