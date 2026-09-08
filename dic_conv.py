import csv
import Data
from pprint import pformat

class Read_csv:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def save_csv(self):

        with (open(self.csv_file_path, newline='') as csvfile):
            reader = csv.DictReader(csvfile)
            list_form = list(reader)
            length = len(list_form)
            if length == 0:
                print("\033[91m" + "Error: One row in a CSV file is not allowed at least two row should be there." + "\033[0m")
            else:
                for row in list_form:
                    if 'Name' in list(row) and 'E-mail' in list(row) and 'ID' in list(row):
                        Data.User_data_1.append(row)

                        with open("Data.py", "w") as file:
                            file.write("User_data_1 = "+pformat(Data.User_data_1))
                    else:
                        print("\033[91m" + "Error: Your dictionary key is not matched, the system requirement name for the first row of csv file should be like : Name,ID,E-mail. Your data will saved with zero data." + "\033[0m")
                        break
                print("Yor data saved successfully! restart your software.")
