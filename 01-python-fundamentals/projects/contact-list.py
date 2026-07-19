"""
Instructions
Project Structure, Rules, and Requirements

We will develop an agenda to save, edit, delete, and mark a contact as a favorite.

The application's output should be displayed in the terminal, as seen in the "Introduction to Python" module.
"""

"""

Tasks

Use this checklist to help organize your delivery

[x] Show a list of options for what can be done with the app and allow the user to type a choice to start the application.

[x] Implement functionality to add a contact (Name, Phone, Email, Favorite)

[x] Develop a view of the list of registered contacts

[ ] Create functionality to edit an existing contact

[ ] Implement an option to mark/unmark a contact as a favorite

[ ] Develop a view of the list of favorite contacts

[ ] Create functionality to delete a contact


"""

def add_contact(agenda, name, phone, email):

  contact = {
    "name": name, 
    "phone": phone, 
    "email": email, 
    "isFavorite": False
  }

  agenda.append(contact)

  print(f"\nContact {contact['name']} - {contact['phone']} was added successfully!")

  return



def show_contact_list(agenda):

  print("\nContact List.")
  
  for index, contact in enumerate(agenda, start=1):
    print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

  return



def edit_contact(agenda, new_contact, index_contact):

  adjusted_index = int(index_contact) - 1

  if (adjusted_index >= 0 and adjusted_index < len(agenda)):
    agenda[adjusted_index]["name"] = new_contact["new_name"]
    agenda[adjusted_index]["phone"] = new_contact["new_phone"]
    agenda[adjusted_index]["email"] = new_contact["new_email"]

    print(f"\nContact updated successfully!")
  
  else:
    print(f"\nYou entered an invalid index!")
 

  return




agenda = []

while True:
  print("\nContact Manager Menu:")
  print("1. Add a new contact")
  print("2. Show contact list")
  print("3. Edit a contact")
  print("4. Mark/unmark a contact as a favorite")
  print("5. Delete a contact")
  print("6. Exit")
  choice = int(input("\nChoose an option to continue: "))

 
  if choice == 1:
    name = input("Enter contact name: ") 
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    add_contact(agenda, name, phone, email)
  
  elif choice == 2:
    show_contact_list(agenda)
  

  elif choice == 3:
    show_contact_list(agenda)
    index_contact = input("Enter the contact number to edit: ")
    new_name = input("Enter contact name: ") 
    new_phone = input("Enter phone number: ")
    new_email = input("Enter email: ")

    new_contact = {
      "new_name": new_name,
      "new_phone": new_phone,
      "new_email": new_email
    }
    edit_contact(agenda, new_contact, index_contact)


  elif choice == 6:
    break


  else:
    print("Sorry! you entered an invalid option. Try again!")






print("Program ended!")



