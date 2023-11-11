from firebase_config import initialize_firebase
from event import Event
from guest_list import GuestList
from rsvp import RSVP

# Initialize Firebase
db = initialize_firebase()


# Example Usage
event_name = input("Enter event name: ")
date = input("Enter event date (YYYY-MM-DD): ")
location = input("Enter event location: ")

event = Event(event_name, date, location)
event_id = event.add_event_to_firestore()
print(f"Event added with ID: {event_id}")

guest_list = GuestList()
guest_name = input("Enter guest name (type 'done' when finished): ")
while guest_name.lower() != 'done':
    guest_list.add_guest(guest_name)
    guest_name = input("Enter guest name (type 'done' when finished): ")

guest_list_id = guest_list.add_guest_list_to_firestore()
print(f"Guest List added with ID: {guest_list_id}")

rsvp = RSVP(event, guest_list)
rsvp_id = rsvp.add_rsvp_to_firestore()
print(f"RSVP added with ID: {rsvp_id}")

# View all data from Firestore
print("\nAll Events:")
for event_id, event_data in Event.get_all_events_from_firestore():
    print(f"Event ID: {event_id}, Data: {event_data}")

print("\nAll Guest Lists:")
for guest_list_id, guest_list_data in GuestList.get_all_guest_lists_from_firestore():
    print(f"Guest List ID: {guest_list_id}, Data: {guest_list_data}")

print("\nAll RSVPs:")
for rsvp_id, rsvp_data in RSVP.get_all_rsvps_from_firestore():
    print(f"RSVP ID: {rsvp_id}, Data: {rsvp_data}")