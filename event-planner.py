from firebase_config import initialize_firebase
from event import Event
from guest_list import GuestList

# Initialize Firebase
db = initialize_firebase()

play = 1
userInput = 0
print('Hello and Welcome to my Event Planner Program.')
while(play == 1):
    print('User Menu:')
    print('1. Add Event')
    print('2. Edit Event')
    print('3. Add Guest List')
    print('4. Edit Guest List')
    print('5. Display Event and Guest List')
    print('6. Delete Event and Guest List')
    print('7. Exit Program')
    
    userInput = input('Enter your choice: ')
    userInput = int(userInput)
    
    # Add Event
    if (userInput == 1):
        
        event_name = input('Enter event name: ')
        date = input('Enter event date (YYYY - MM- DD): ')
        location = input('Enter event location: ')
        event = Event(event_name, date, location)
        
        event_id = event.add_event_to_firestore()
        print(f'Event added with ID: {event_id}\n')
    
    # Edit Event
    if (userInput == 2):
        
        event_id_to_edit = input("Enter the ID of the event you want to edit: ")

        # Retrieve the event from Firestore using the provided ID
        event_ref = db.collection('events').document(event_id_to_edit)
        existing_event = event_ref.get()

        if existing_event.exists:
            # Display existing event details
            print(f'Existing Event Details:\n{existing_event.to_dict()}')

            # Capture new details from the user
            event_name = input('Enter new event name: ')
            date = input('Enter new event date (YYYY-MM-DD): ')
            location = input('Enter new event location: ')

            # Update the event in Firestore
            event_ref.update({
                'name': event_name,
                'date': date,
                'location': location
            })

            print('Event updated successfully!\n')
        else:
            print(f'Event with ID {event_id_to_edit} not found.\n')
        
    # Add Guest List
    if (userInput == 3):
        
        guest_list = GuestList()

        guest_name = input("Enter guest name (type 'done' when finished): ")
        while guest_name.lower() != 'done':
            guest_list.add_guest(guest_name)
            guest_name = input('Enter guest name: ')

        guest_list_id = guest_list.add_guest_list_to_firestore()
        print(f'Guest List added with ID: {guest_list_id}\n')

    
    # Edit Guest List
    if (userInput == 4):
        
        guest_list_id_to_edit = input("Enter the ID of the guest list you want to edit: ")

        # Retrieve the guest list from Firestore using the provided ID
        guest_list_ref = db.collection('guest_lists').document(guest_list_id_to_edit)
        existing_guest_list = guest_list_ref.get()

        if existing_guest_list.exists:
            # Display existing guest list details
            print(f'Existing Guest List Details:\n{existing_guest_list.to_dict()}')

            # Capture new details from the user
            new_guest_list = GuestList()

            guest_name = input("Enter new guest name (type 'done' when finished): ")
            while guest_name.lower() != 'done':
                new_guest_list.add_guest(guest_name)
                guest_name = input('Enter new guest name (type \'done\' when finished): ')

            # Update the guest list in Firestore
            guest_list_ref.update({
                'guests': new_guest_list.guests
            })

            print('Guest List updated successfully!\n')
        else:
            print(f'Guest List with ID {guest_list_id_to_edit} not found.\n')
    
    if (userInput == 5):
        
        event_id_to_display = input("Enter the ID of the event to display: ")

        # Retrieve the event from Firestore using the provided ID
        event_ref = db.collection('events').document(event_id_to_display)
        existing_event = event_ref.get()

        if existing_event.exists:
            # Display event details
            print(f'Event ID: {event_id_to_display}, Event Details: {existing_event.to_dict()}')

            # Prompt user for the guest list ID
            guest_list_id = input("Enter the ID of the guest list to display: ")
            guest_list_details = GuestList.get_guest_list_by_id(guest_list_id)
            print(f'Guest List Details: {guest_list_details}\n')

        else:
            print(f'Event with ID {event_id_to_display} not found.\n')
            
    if (userInput == 6):
        
        event_id_to_delete = input("Enter the ID of the event to delete along with its associated guest list: ")

        # Retrieve the event from Firestore using the provided ID
        event_ref = db.collection('events').document(event_id_to_delete)
        existing_event = event_ref.get()

        if existing_event.exists:
            # Retrieve the associated guest list ID
            guest_list_id_associated = existing_event.get('guest_list_id')

            # Delete the event from Firestore
            event_ref.delete()
            print(f'Event with ID {event_id_to_delete} deleted successfully.\n')

            # Delete the associated guest list using the guest list ID
            if guest_list_id_associated:
                guest_list_ref = db.collection('guest_lists').document(guest_list_id_associated)
                guest_list_ref.delete()
                print(f'Associated Guest List with ID {guest_list_id_associated} deleted.\n')
            else:
                print('No associated guest list.\n')

        else:
            print(f'Event with ID {event_id_to_delete} not found.\n')
    
    if (userInput == 7):
        print('Thank you. Exiting Program.')
        play = 0