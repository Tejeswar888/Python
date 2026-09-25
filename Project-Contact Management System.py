contacts = {}

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Remove Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        mobile = input("Enter mobile: ")
        email = input("Enter email: ")

        contacts[name] = {
            "mobile": mobile,
            "email": email
        }

        print("Contact added successfully")

    elif choice == 2:
        name = input("Enter name to update: ")

        if name in contacts:
            contacts[name]["mobile"] = input("Enter new mobile: ")
            contacts[name]["email"] = input("Enter new email: ")
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == 3:
        if not contacts:
            print("No contacts available")
        else:
            print("\n--- Contacts ---")
            for name, details in contacts.items():
                print("Name:", name)
                print("Mobile:", details["mobile"])
                print("Email:", details["email"])
                print("----------------")

    elif choice == 4:
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == 5:
        print("Program stopped")
        break

    else:
        print("Invalid choice")