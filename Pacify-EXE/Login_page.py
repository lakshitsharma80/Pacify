import Data
import os
import sys

# Get the correct directory (works with .exe and normal Python)
if getattr(sys, 'frozen', False):
    # Running as compiled .exe
    script_dir = os.path.dirname(sys.executable)
else:
    # Running as normal Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))

data_file = os.path.join(script_dir, "Data.py")

class Login_Section:
    def __init__(self):
        self.login = True
    
    def ASK_AND_STORE(self):

        while self.login:
            self.students = int(input("How many object are there?: "))
            
            if self.students == 0:
                print("No data to save Invalid number of objects '0' is not defined. Try again!")
            else:
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
                    with open(data_file, "w") as file:
                        file.write("User_data_1 = [\n")
                        for user in Data.User_data_1:
                            file.write("     {\n")
                            file.write(f"         'Name': '{user["Name"]}', \n")
                            file.write(f"         'ID': '{user["ID"]}', \n")
                            file.write(f"         'E-mail': '{user["E-mail"]}'\n")
                            file.write("     },\n")
                        file.write("]\n")

                self.login = False
                print("Your data successfully saved! Restart your software again for those changes.")


    def CLEAR_DATA(self):
        with open(data_file, "w") as file:
            file.write("User_data_1 = []")
        print("Your data removed successfully! Restart your software again for those changes.")

