import Data
from pprint import pformat

class Login_Section:
    def __init__(self):
        self.login = True
    
    def ASK_AND_STORE(self):
        while self.login:
            self.students = int(input("How many object are there?: "))
            if self.students == 0:
                print("No data to save Invalid number of objects '0' is not defined. Try again!")
            else:
                self.api_key = input("Enter your API KEY for using AI model (NVIDIA_MODELS/Meta/llama-3.1-8b-instruct)/It is option you can just type 'skip-api or 'sk-a' if you don't want to use AI model: ")
                if self.api_key == "skip-api" or self.api_key == "sk-a":
                    with open("API_KEY.txt","w") as file:
                        file.write("none")
                else:
                    with open("API_KEY.txt","w") as file:
                        file.write(self.api_key)
                                    
                for i in range(self.students):
                    self.name = input(f"Enter the name of object {i+1}: ")
                    self.id = input(f"Enter the ID of object {i+1} or you can create the ID: ")
                    self.email = input(f"Enter the email of object {i+1}: ")
                    # Store in Data.py
                    Data.User_data_1.append({
                        "Name": self.name,
                        "ID": self.id,
                        "E-mail": self.email
                    })

                    # Write data into Data.py
                    with open("Data.py","w") as file:
                        file.write("User_data_1 = [\n")
                        for user in Data.User_data_1:
                            file.write("     {\n")
                            file.write(f"         'Name': '{user["Name"]}', \n")
                            file.write(f"         'ID': '{user["ID"]}', \n")
                            file.write(f"         'E-mail': '{user["E-mail"]}'\n")
                            file.write("     },\n")
                        file.write("]\n")

                print("Your data successfully saved! Restart your software again for those changes.")
                self.login = False

    def CLEAR_DATA(self):
        with open("Data.py", "w") as file:
            file.write("User_data_1 = []")
        
        with open("API_KEY.txt", "w") as file:
            file.write("none")
        print("Your data removed successfully! Restart your software again for those changes.")

