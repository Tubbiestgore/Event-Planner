from firebase_config import initialize_firebase

# Access Firestore database
db = initialize_firebase()

class Event:
    def __init__(self, event_name, date, location):
        self.event_name = event_name
        self.date = date
        self.location = location

    def to_dict(self):
        return {
            'name': self.event_name,
            'date': self.date,
            'location': self.location
        }

    def add_event_to_firestore(self):
        events_ref = db.collection('events')
        doc_ref = events_ref.add(self.to_dict())
        
        # Extract the document ID from the tuple
        doc_id = doc_ref[1].id if isinstance(doc_ref, tuple) else doc_ref.id

        return doc_id

    @staticmethod
    def get_all_events_from_firestore():
        events_ref = db.collection('events').stream()
        return [(event.id, event.to_dict()) for event in events_ref]