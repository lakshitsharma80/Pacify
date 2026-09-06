import csv
import Data
from pprint import pformat

class Read_csv:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def save_csv(self):
        with open(self.csv_file_path, newline='') as csvfile:
            a = csv.DictReader(csvfile)
            for row in a:
                Data.User_data_1.append(row)

                with open("Data.py", "w") as file:
                    file.write("User_data_1 = "+pformat(Data.User_data_1))

