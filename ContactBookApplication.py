# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
        print("Address:", contacts[name]["address"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Closing Contact Book.")
        break
    else:
        print("Invalid choice.")