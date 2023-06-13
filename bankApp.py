import random
import json

file_name = "Data.json"

# Functions
def intro():
    print("\t\t\t\t********")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t********")

    print("\t\t\t\tBrought To You By:")
    print("\t\t\t\tSHREYAN NAG COMPUTER CLASSES")
    input()


def details(name, dictionary):
    if name in dictionary:
        print()
        print("Details:")
        print("Name:", name)
        print("ID:", dictionary[name]["ID"])
        print("Account Number:", dictionary[name]["Account Number"])
        print("Balance:", dictionary[name]["Balance"])
    else:
        print("Account not found.")


def update_account(name, editing, value, dictionary):
    if name in dictionary:
        print()
        dictionary[name][editing] = value
        print(f"{editing} has been changed to {value} successfully.")
        return True
    else:
        print("Account not found.")
        return False


# Start of the program
intro()

while True:
    print("\tMAIN MENU")
    print("\t1. ADD AN ACCOUNT")
    print("\t2. UPDATE ACCOUNT")
    print("\t3. ACCOUNT DETAILS")
    print("\t4. EXIT")
    print()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num_entries = int(input("Enter the number of individual entries: "))
        data = {}

        for _ in range(num_entries):
            print()
            fname = input("Enter Full Name: ")
            nested_account = input("Enter Account Number: ")
            nested_balance = input("Enter Balance: ")
            nested_id = int(random.random() * 1000000000)
            nd = {
                'ID': nested_id,
                'Account Number': nested_account,
                'Balance': nested_balance
            }
            data[fname] = nd

        try:
            with open(file_name, "r") as file:
                present = json.load(file)
                present.update(data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            present = data

        with open(file_name, "w") as file:
            json.dump(present, file, indent=1)

    elif choice == 2:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)

            information = input("Whose account requires updating? [Enter Name]: ")
            if information in data:
                editing = input("What do you want to edit, Balance or Account Number? [Capitalization Sensitive]: ")
                new_value = input("Enter the new amount: ")
                update_account(information, editing, new_value, data)
                with open(file_name, "w") as file:
                    json.dump(data, file, indent=1)
            else:
                print("Account not found.")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Data file is empty. Add an account first.")

    elif choice == 3:
        try:
            with open(file_name, "r") as file:
                data = json.load(file)

            name = input("Enter Account Holder name: ")
            details(name, data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Data file is empty. Add an account first.")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.\n")
