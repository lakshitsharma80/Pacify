import Data
from pprint import pformat


class Login_Section:
    def __init__(self):
        self.login = True

    def ASK_AND_STORE(self):

        # Making these var into global statement.
        global fields, no_fields, value
        while self.login:
            self.objects = int(input("How many object are there: "))

            if self.objects == 0:
                print("No data to save Invalid number of objects '0' is not defined. Try again!")
            else:
                self.api_key = input(
                    "Enter your API KEY for using AI model (NVIDIA_MODELS/Meta/llama-3.1-8b-instruct)/It is optional you can just type 'skip-api or 'sk-a' if you don't want to use AI model: ")
                if self.api_key == "skip-api" or self.api_key == "sk-a":
                    with open("API_KEY.txt", "w") as file:
                        file.write("none")
                else:
                    with open("API_KEY.txt", "w") as file:
                        file.write(self.api_key)

                # Row adding function
                row_ask = input("Did you want to add another fields of data (y/n): ").lower()
                if row_ask == "y":
                    fields = []
                    no_fields = int(input("How many fields of data do you want: "))

                    for rows in range(no_fields):
                        field_name = input(f"Enter field name of {rows + 1}: ")
                        fields.append(field_name)

                for i in range(self.objects):
                    self.name = input(f"Enter the name of object {i + 1}: ")
                    self.id = input(f"Enter the ID of object {i + 1} or you can create the ID: ")
                    self.email = input(f"Enter the email of object {i + 1}: ")

                    if fields:
                        value = []
                        for name in range(no_fields):
                            self.name_value = input(f"Enter field value of {name + 1}: ")
                            value.append(self.name_value)

                    # Store in Data.py
                    Data.User_data_1.append({
                        "Name": self.name,
                        "ID": self.id,
                        "E-mail": self.email,
                    })

                    if fields:
                        for f in range(no_fields):
                            Data.User_data_1[i][f"{fields[f]}"] = value[f]

                    # Write data into Data.py
                    with open("Data.py", "w") as file:
                        file.write("User_data_1 = " + pformat(Data.User_data_1))

                print("Your data successfully saved! Restart your software again for those changes.")
                self.login = False

    def CLEAR_DATA(self):
        with open("Data.py", "w") as file:
            file.write("User_data_1 = []")

        with open("API_KEY.txt", "w") as file:
            file.write("none")
        print("Your data removed successfully! Restart your software again for those changes.")

