import json

# File to store contacts
contact_file = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(contact_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(contact_file, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!\n")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return

    print("\n--- Contact List ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")
    print()

# Search for a contact
def search_contact(contacts):
    search_query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_query in contact["name"] or search_query in contact["phone"]]

    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        print()
    else:
        print("No matching contacts found.\n")

# Update an existing contact
def update_contact(contacts):
    search_query = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"] == search_query:
            print("Leave fields blank to keep the current value.")
            contact["name"] = input(f"New name ({contact['name']}): ") or contact["name"]
            contact["phone"] = input(f"New phone ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"New email ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"New address ({contact['address']}): ") or contact["address"]

            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")

# Delete a contact
def delete_contact(contacts):
    search_query = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == search_query:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
