contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def view_contacts():
    print("Contacts:")
    for name, contact_info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
        print()

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

    
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        new_phone = input("Enter the new phone number (leave blank if unchanged): ")
        new_email = input("Enter the new email address (leave blank if unchanged): ")

        if new_phone:
            contacts[name]["phone"] = new_phone
        if new_email:
            contacts[name]["email"] = new_email

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete")
    print("4. Update")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        delete_contact()
    elif choice == 4:

        delete_contact()