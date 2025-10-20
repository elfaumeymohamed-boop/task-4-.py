# Create the dictionary
contacts = {
    "Ahmed": "01012345678",
    "Sara": "01198765432",
    "Mahmoud": "01234567890"
}

# Print all contact names
print("Contact names:")
for name in contacts:
    print(name)

# Search for a contact (case-insensitive)
search_name = input("Enter the name you want to search for: ")

# Normalize input and keys to lowercase
found = False
for name in contacts:
    if name.lower() == search_name.lower():
        print(f"{name}'s phone number: {contacts[name]}")
        found = True
        break

if not found:
    print("Name not found in the contact book.")