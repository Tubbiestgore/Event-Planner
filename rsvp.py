from firebase_config import initialize_firebase

# Access Firestore database
db = initialize_firebase()

class RSVP:
    def __init__(self, event, guest_list):
        self.event = event
        self.guest_list = guest_list

    def to_dict(self):
        return {
            'event': self.event.to_dict(),
            'guest_list': self.guest_list.to_dict()
        }

    def add_rsvp_to_firestore(self):
        rsvp_ref = db.collection('rsvps')
        doc_ref = rsvp_ref.add(self.to_dict())

        # Extract the document ID from the tuple
        doc_id = doc_ref[1].id if isinstance(doc_ref, tuple) else doc_ref.id

        return doc_id

    @staticmethod
    def get_all_rsvps_from_firestore():
        rsvps_ref = db.collection('rsvps').stream()
        return [(rsvp.id, rsvp.to_dict()) for rsvp in rsvps_ref]