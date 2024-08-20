class Hospital:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.gender = ""
        self.date = ""
        self.conditions = {
            "Normal wound": 250,
            "Medium wound": 500,
            "Extreme wound": 1000
        }

    def person_detail(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender (Male/Female): ")
        self.date = input("Date (DD/MM/YYYY): ")

    def validate(self):
        # Name validation
        if not self.name.isalpha() or len(self.name) < 6:
            print("Enter a valid name.")
            return False

        # Gender validation
        if self.gender not in ["Male", "Female"]:
            print("Enter a valid gender.")
            return False

        # Age validation
        if not self.age.isdigit() or int(self.age) <= 0:
            print("Enter a valid age.")
            return False

        # Date validation (You may want to use regex or a date library for stricter validation)
        if len(self.date.split('/')) != 3:
            print("Enter the date in DD/MM/YYYY format.")
            return False

        return True

    def get_condition(self):
        condition = input("\nEnter the type of wound of your patient: ")
        if condition in self.conditions:
            print(f"Bill: {self.conditions[condition]}")
            return condition
        else:
            print("Invalid wound type entered.")
            return None

    def save_receipt(self, condition):
        with open(f"{self.name}_Hospital_receipt.txt", "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Gender: {self.gender}\n")
            file.write(f"Date: {self.date}\n")
            file.write(f"{self.name} has a {condition}\n")
            file.write(f"Your Bill: {self.conditions[condition]}\n")

    def main(self):
        self.person_detail()
        if self.validate():  # Only continue if the validation is successful
            condition = self.get_condition()
            if condition:
                self.save_receipt(condition)


if __name__ == "__main__":
    hospital = Hospital()
    hospital.main()

            
           
          

        