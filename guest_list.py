from firebase_config import initialize_firebase

# Access Firestore database
db = initialize_firebase()

class GuestList:
    def __init__(self):
        self.guests = []

    def add_guest(self, guest_name):
        self.guests.append(guest_name)

    def to_dict(self):
        return {'guests': self.guests}

    def add_guest_list_to_firestore(self):
        guest_list_ref = db.collection('guest_lists')
        doc_ref = guest_list_ref.add(self.to_dict())

        # Extract the document ID from the tuple
        doc_id = doc_ref[1].id if isinstance(doc_ref, tuple) else doc_ref.id

        return doc_id
    
    @staticmethod
    def get_guest_list_by_id(guest_list_id):
        guest_list_ref = db.collection('guest_lists').document(guest_list_id)
        guest_list_doc = guest_list_ref.get()

        if guest_list_doc.exists:
            return guest_list_doc.to_dict()
        else:
            return None

    @staticmethod
    def get_all_guest_lists_from_firestore():
        guest_lists_ref = db.collection('guest_lists').stream()
        return [(guest_list.id, guest_list.to_dict()) for guest_list in guest_lists_ref]